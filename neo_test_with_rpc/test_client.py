from typing import List, Union, Dict, Any
import base64
import json
import requests
from neo_test_with_rpc.retry import retry

from tests.utils import Hash160Str, Hash256Str, PublicKeyStr, Signer
from neo3.core.types import UInt160, UInt256
from neo3.contracts import NeoToken, GasToken

neo, gas = NeoToken(), GasToken()

RequestExceptions = (
    requests.RequestException,
    requests.ConnectionError,
    requests.HTTPError,
    requests.Timeout,
)
request_timeout = None  # 20


class TestClient:
    def __init__(self, target_url: str, contract_scripthash: Hash160Str, wallet_scripthash: Hash160Str,
                 wallet_address: Hash160Str,
                 wallet_path: str, wallet_password: str, with_print=True, session=requests.Session()):
        """

        :param target_url: url to the rpc server affliated to neo-cli
        :param wallet_scripthash: scripthash of your wallet
        :param wallet_address: address of your wallet (starting with 'N'); "NVbGwMfRQVudTjWAUJwj4K68yyfXjmgbPp"
        :param wallet_path: 'wallets/dev.json'
        :param wallet_password: '12345678'
        :param session: requests.Session
        """
        self.target_url = target_url
        self.contract_scripthash = contract_scripthash
        self.session = session
        self.wallet_scripthash = wallet_scripthash
        self.signer = Signer(wallet_scripthash)
        self.wallet_address = wallet_address
        self.wallet_path = wallet_path
        self.wallet_password = wallet_password
        self.previous_post_data = None
        self.with_print = with_print
    
    @staticmethod
    def request_body_builder(method, parameters: List):
        return json.dumps({
            "jsonrpc": "2.0",
            "method": method,
            "params": parameters,
            "id": 1,
        }, separators=(',', ':'))
    
    @staticmethod
    def bytes_to_UInt160(bytestring: bytes):
        return Hash160Str.from_UInt160(UInt160.deserialize_from_bytes(bytestring))
    
    @staticmethod
    def base64_struct_to_bytestrs(base64_struct: dict) -> List[bytes]:
        processed_struct = []
        if type(base64_struct) is dict and 'type' in base64_struct and base64_struct['type'] == 'Struct':
            values = base64_struct['value']
            for value in values:
                if value['type'] == 'ByteString':
                    processed_struct.append(base64.b64decode(value['value']))
        return processed_struct
    
    @retry(RequestExceptions, tries=2, logger=None)
    def meta_rpc_method(self, method: str, parameters: List, relay: bool = True, do_not_raise_on_result=False) -> Any:
        post_data = self.request_body_builder(method, parameters)
        self.previous_post_data = post_data
        result = json.loads(self.session.post(self.target_url, post_data, timeout=request_timeout).text)
        if 'error' in result:
            raise ValueError(result['error']['message'])
        if type(result['result']) is dict:
            if 'exception' in result['result'] and result['result']['exception'] != None:
                if do_not_raise_on_result:
                    return result['result']['exception']
                else:
                    print(post_data)
                    print(result)
                    raise ValueError(result['result']['exception'])
            if relay and 'tx' in result['result']:
                tx = result['result']['tx']
                self.sendrawtransaction(tx)
        self.previous_raw_result = result
        self.previous_result = self.parse_raw_result(result)
        return self.previous_result
    
    def print_previous_result(self):
        print(self.previous_result)
    
    @retry(RequestExceptions, tries=2, logger=None)
    def sendrawtransaction(self, transaction: str):
        """
        :param transaction: result['tx']. e.g. "ALmNfAb4lqIAAA...="
        """
        return self.meta_rpc_method("sendrawtransaction", [transaction], relay=False)
    
    def openwallet(self, path: str = None, password: str = None) -> dict:
        """
        WARNING: usually you should use this method along with __init__.
        Use another TestClient object to open another wallet
        """
        if not path:
            path = self.wallet_path
        if not password:
            password = self.wallet_password
        open_wallet_result = self.meta_rpc_method("openwallet", [path, password])
        if open_wallet_result != True:
            raise ValueError(f'Failed to open wallet {path} with given password.')
        return open_wallet_result
    
    @staticmethod
    def parse_raw_result(raw_result: dict):
        def parse_single_item(item: Union[Dict, List]):
            if 'iterator' in item:
                item = item['iterator']
                return {parse_single_item(i['value'][0]): parse_single_item(i['value'][1]) for i in item}
            type = item['type']
            if type == 'Any' and 'value' not in item:
                return
            else:
                value = item['value']
            if type == 'Integer':
                return int(value)
            elif type == 'Boolean':
                return value
            elif type == 'ByteString':
                try:
                    return base64.b64decode(value).decode()
                except UnicodeDecodeError as e:
                    # may be an N3 address starting with 'N'
                    # TODO: decode to N3 address
                    return value
            elif type == 'Array':
                return [parse_single_item(i) for i in value]
            elif type == 'Map':
                return {parse_single_item(i['key']): parse_single_item(i['value']) for i in value}
            else:
                raise ValueError(f'Unknown type {type}')
        
        result: Dict = raw_result['result']
        if type(result) is not dict or 'stack' not in result:
            return result
        result: List = result['stack'][0]
        return parse_single_item(result)
    
    def invokefunction_of_any_contract(self, scripthash: Hash160Str, operation: str,
                                       params: List[Union[str, int, Hash160Str, UInt160]] = None,
                                       signers: List[Signer] = None, relay=True, do_not_raise_on_result=False) -> dict:
        if self.with_print:
            print(f'invoke function {operation}')
        
        def parse_params(param: Union[str, int, Hash160Str, UInt160, bytes]) -> Dict[str, str]:
            type_param = type(param)
            if type_param is UInt160:
                return {
                    'type': 'Hash160',
                    'value': str(Hash160Str.from_UInt160(param)),
                }
            elif type_param is Hash160Str:
                return {
                    'type': 'Hash160',
                    'value': str(param),
                }
            elif type_param is UInt256:
                    return {
                        'type': 'Hash256',
                        'value': str(Hash256Str.from_UInt256(param)),
                    }
            elif type_param is Hash256Str:
                return {
                    'type': 'Hash256',
                    'value': str(param),
                }
            elif type_param is PublicKeyStr:
                return {
                    'type': 'PublicKey',
                    'value': str(param),
                }
            elif type_param is int:
                return {
                    'type': 'Integer',
                    'value': str(param),
                }
            elif type_param is str:
                return {
                    'type': 'String',
                    'value': param,
                }
            elif type_param is bytes:
                # not the best way to judge, but maybe no better method
                try:
                    return {
                        'type': 'String',
                        'value': param.decode(),
                    }
                except UnicodeDecodeError:
                    return {
                        'type': 'ByteArray',
                        'value': base64.b64encode(param).decode()
                    }
            elif type_param is list:
                return {
                    'type': 'Array',
                    'value': [parse_params(param_) for param_ in param]
                }
            raise ValueError(f'Unable to handle param {param} with type {type_param}')
        
        if not params:
            params = []
        if not signers:
            signers = [self.signer]
        parameters = [
            str(scripthash),
            operation,
            list(map(lambda param: parse_params(param), params)),
            list(map(lambda signer: signer.to_dict(), signers)),
        ]
        result = self.meta_rpc_method('invokefunction', parameters, relay=relay,
                                      do_not_raise_on_result=do_not_raise_on_result)
        return result
    
    def invokefunction(self, operation: str, params: List[Union[str, int, Hash160Str, UInt160]] = None,
                       signers: List[Signer] = None, relay=True, do_not_raise_on_result=False) -> dict:
        return self.invokefunction_of_any_contract(self.contract_scripthash, operation, params,
                                                   signers, relay=relay, do_not_raise_on_result=do_not_raise_on_result)
    
    def sendfrom(self, asset_id: Hash160Str, from_address: str, to_address: str, value: int,
                 signers: List[Signer] = None):
        """

        :param asset_id: NEO: '0xef4073a0f2b305a38ec4050e4d3d28bc40ea63f5';
            GAS: '0xd2a4cff31913016155e38e474a2c06d08be276cf'
        :param from_address: "NgaiKFjurmNmiRzDRQGs44yzByXuSkdGPF"
        :param to_address: "NikhQp1aAD1YFCiwknhM5LQQebj4464bCJ"
        :param value: 100000000, including decimals
        :param signers:
        :return:
        """
        if not signers:
            signers = [self.signer]
        return self.meta_rpc_method('sendfrom', [
            asset_id.to_str(),
            from_address, to_address, value,
            signers
        ])
    
    def sendtoaddress(self, asset_id: Hash160Str, address, value: int):
        return self.meta_rpc_method('sendtoaddress', [
            asset_id.string, address, value,
        ])
    
    def send_neo_to_address(self, to_address: Hash160Str, value: int):
        return self.sendtoaddress(Hash160Str.from_UInt160(NeoToken().hash), to_address, value)
    
    def send_gas_to_address(self, to_address: Hash160Str, value: int):
        return self.sendtoaddress(Hash160Str.from_UInt160(GasToken().hash), to_address, value)
    
    def getwalletbalance(self, asset_id: Hash160Str) -> int:
        return int(self.meta_rpc_method('getwalletbalance', [asset_id.to_str()])['balance'])
    
    def get_neo_balance(self) -> int:
        return self.getwalletbalance(Hash160Str.from_UInt160(NeoToken().hash))
    
    def get_gas_balance(self) -> int:
        return self.getwalletbalance(Hash160Str.from_UInt160(GasToken().hash))
    
    def get_rToken_balance(self, rToken_address: Hash160Str):
        return self.invokefunction_of_any_contract(rToken_address, "balanceOf", [self.wallet_scripthash])
