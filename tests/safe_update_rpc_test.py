import json

from tests.config import safe_contract_hash

from neo_test_with_rpc import TestClient
from tests.utils import Hash160Str, sleep_for_next_block


target_url = 'http://127.0.0.1:10332'

wallet_address = 'Nb2CHYY5wTh2ac58mTue5S3wpG6bQv5hSY'
wallet_hash = Hash160Str('0xb1983fa2479a0c8e2beae032d2df564b5451b7a5')

with open('../AnyContract.nef', 'rb') as f:
    nef_file = f.read()
with open('../AnyContract.manifest.json', 'r') as f:
    manifest_dict = json.loads(f.read())
    manifest_dict['name'] = 'AnyUpdateSafe'
    manifest = json.dumps(manifest_dict, separators=(',', ':'))

client = TestClient(target_url, safe_contract_hash, wallet_hash, wallet_address, 'testnet.json', '1')
client.openwallet()
client.invokefunction('putStorage', params=["original_nef_file", "testValue"], do_not_raise_on_result=True)
client.invokefunction('putStorage', params=["original_manifest", "testValue"], do_not_raise_on_result=True)
client.invokefunction('putStorage', params=["testKey", "testValue"])
sleep_for_next_block()
client.invokefunction('anyUpdate0', params=[nef_file, manifest, 'putNef'])
client.print_previous_result()
sleep_for_next_block()
client.invokefunction('getStorage', params=['original_nef_file'], relay=False)
client.print_previous_result()
client.invokefunction('anyUpdate1', params=[nef_file, manifest, 'hello1', 1])
client.print_previous_result()
sleep_for_next_block()
client.invokefunction('anyUpdate0', params=[nef_file, manifest, 'helloNeo'])
client.print_previous_result()
sleep_for_next_block()
client.invokefunction('getStorage', params=["testKey"], relay=False)
client.print_previous_result()