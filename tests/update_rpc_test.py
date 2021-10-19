import json

from tests.config import contract_hash

from neo_test_with_rpc import TestClient
from tests.utils import Hash160Str, sleep_for_next_block


target_url = 'http://127.0.0.1:10332'

wallet_address = 'Nb2CHYY5wTh2ac58mTue5S3wpG6bQv5hSY'
wallet_hash = Hash160Str('0xb1983fa2479a0c8e2beae032d2df564b5451b7a5')

with open('../AnyContract.nef', 'rb') as f:
    nef_file = f.read()
with open('../AnyContract.manifest.json', 'r') as f:
    manifest_dict = json.loads(f.read())
    manifest_dict['name'] = 'AnyUpdate'
    manifest = json.dumps(manifest_dict, separators=(',', ':'))

client = TestClient(target_url, contract_hash, wallet_hash, wallet_address, 'testnet.json', '1')
client.openwallet()
client.invokefunction('anyUpdate0', params=[nef_file, manifest, 'helloNeo'])
client.print_previous_result()
sleep_for_next_block()
client.invokefunction('anyUpdate0', params=[nef_file, manifest, 'helloNeo'])
client.print_previous_result()
