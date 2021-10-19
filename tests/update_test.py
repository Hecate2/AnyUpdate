from neo_test_with_vm import TestEngine
import json, hashlib


engine = TestEngine('../AnyUpdate.nef')

with open('../AnyContract.nef', 'rb') as f:
    nef_file = f.read()
with open('../AnyContract.manifest.json', 'r') as f:
    manifest_dict = json.loads(f.read())
    manifest_dict['name'] = 'AnyUpdate'
    manifest = json.dumps(manifest_dict, separators=(',', ':'))

print(engine.manifest.abi.methods[-1].offset)
cut_nef_without_checksum = engine.raw_nef[:len(engine.raw_nef)-4-(len(engine.nef.script)-engine.manifest.abi.methods[-1].offset)]
print(cut_nef_without_checksum)
checksum = hashlib.sha256(hashlib.sha256(cut_nef_without_checksum).digest()).digest()[:4]
print(cut_nef_without_checksum + checksum)
print(engine.raw_nef)
print(json.dumps(engine.raw_manifest))

engine._deploy_with_print([None, False])
engine.anyUpdate0_with_print([nef_file, manifest, 'helloNeo'])
engine.anyUpdate0_with_print([nef_file, manifest, 'helloNeo'])
engine.anyUpdate0_with_print([nef_file, manifest, 'helloNeo'])
