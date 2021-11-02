import json

from tests.config import renter_contract_hash, contract_for_rent_hash

from neo_test_with_rpc import TestClient
from tests.utils import Hash160Str, sleep_for_next_block, Signer, WitnessScope


target_url = 'http://127.0.0.1:10332'

wallet_address = 'Nb2CHYY5wTh2ac58mTue5S3wpG6bQv5hSY'
wallet_hash = Hash160Str('0xb1983fa2479a0c8e2beae032d2df564b5451b7a5')
user1_address = 'NaainHz563mJLsHRsPD4NrKjMEQGBXXJY9'
user1_hash = Hash160Str('0x1f5a2928e0a05fdfba45e5f1b55fd6a88df5e5a0')

with open('../AnyContract.nef', 'rb') as f:
    nef_file = f.read()
with open('../AnyContract.manifest.json', 'r') as f:
    manifest_dict = json.loads(f.read())
    manifest_dict['name'] = 'AnyUpdateSafeRent'
    manifest = json.dumps(manifest_dict, separators=(',', ':'))

signer = Signer(wallet_hash, scopes=WitnessScope.Global)
client = TestClient(target_url, renter_contract_hash, wallet_hash, wallet_address, 'testnet.json', '1')
client.openwallet()
client.invokefunction('setOwner', params=[wallet_hash], relay=False)
client.invokefunction('requestRental', params=[wallet_hash, -1], do_not_raise_on_result=True, relay=False)
client.invokefunction('readContractAddress', relay=False)
client.print_previous_result()
client.invokefunction('registerContract', params=[0, contract_for_rent_hash])
client.invokefunction('registerContract', params=[1, contract_for_rent_hash])
sleep_for_next_block()
client.invokefunction('readContractAddress', relay=False)
client.print_previous_result()
client.invokefunction('unregisterContract', params=[1])
sleep_for_next_block()
client.invokefunction('readContractAddress', relay=False)
client.print_previous_result()
client.invokefunction('requestRental', params=[wallet_hash, wallet_hash, -1], relay=False, signers=[signer], do_not_raise_on_result=True)
client.invokefunction('requestRental', params=[wallet_hash, wallet_hash, 100000], signers=[signer])
client.print_previous_result()
sleep_for_next_block()
client.invokefunction_of_any_contract(contract_for_rent_hash, 'anyUpdate', [nef_file, manifest, 'hello1', [1]], relay=False)
client.print_previous_result()
client.invokefunction_of_any_contract(contract_for_rent_hash, 'anyUpdate0', [nef_file, manifest, 'putNef'], relay=False)
client.print_previous_result()

user1_signer = Signer(user1_hash, scopes=WitnessScope.Global)
user1client = TestClient(target_url, renter_contract_hash, user1_hash, user1_address, 'user1.json', '1')
user1client.openwallet()
user1client.invokefunction_of_any_contract(contract_for_rent_hash, 'anyUpdate0', [nef_file, manifest, 'putNef'], do_not_raise_on_result=True)
user1client.invokefunction('requestRental', params=[user1_hash, user1_hash, 100000], signers=[user1_signer])
user1client.print_previous_result()
