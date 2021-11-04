from tests.utils import Hash160Str

contract_hash = Hash160Str('0x68740b907e4fcb265c5ad339c38251b6f843577a')
safe_contract_hash = Hash160Str('0xb0b0d4bad5a8c17967ee30d997f0f1759c742402')
short_contract_hash = Hash160Str('0x7cfe35715b3b2b9f3bc696f7483077434158d601')
short_safe_contract_hash = Hash160Str('0x5c1068339fae89eb1a743909d0213e1d99dc5dc9')
renter_contract_hash = Hash160Str('0x9cf19e43333a0b4513bd61e2316b40ecb9454a9b')
_ = bytearray(bytes.fromhex(renter_contract_hash.string[2:]))
_.reverse()
print(_)
contract_for_rent_hash0 = Hash160Str('0xb82bb0da46129f219d657cb6d7fbb22415efc502')
contract_for_rent_hash1 = Hash160Str('0x6d13f393c90fa7182974a2b4d212e82bd0ccaf24')
contract_for_rent_hash2 = Hash160Str('0xc2319a0e9c469598ba8c9425b56bcc39315c4c3e')