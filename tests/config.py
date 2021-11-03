from tests.utils import Hash160Str

contract_hash = Hash160Str('0x68740b907e4fcb265c5ad339c38251b6f843577a')
safe_contract_hash = Hash160Str('0xb0b0d4bad5a8c17967ee30d997f0f1759c742402')
short_contract_hash = Hash160Str('0x01918c892feb3056994aa4f70640d7b978eb2c5d')
short_safe_contract_hash = Hash160Str('0xbb0bfd9b5f1cdab4318012ff80b6f0c51778a2d4')
renter_contract_hash = Hash160Str('0x9cf19e43333a0b4513bd61e2316b40ecb9454a9b')
_ = bytearray(bytes.fromhex(renter_contract_hash.string[2:]))
_.reverse()
print(_)
contract_for_rent_hash = Hash160Str('0xb82bb0da46129f219d657cb6d7fbb22415efc502')