from tests.utils import Hash160Str

contract_hash = Hash160Str('0x7882ab97bb1d89b5bdcbbc50be1cc981eb594aeb')
safe_contract_hash = Hash160Str('0x52aabe7814458f83eb8197dcce68ff30597c37d3')
short_contract_hash = Hash160Str('0x643a7a9bb8e051ed35546ce146982a7ca9468c5f')
short_safe_contract_hash = Hash160Str('0x2bf858b5c244a6cb5463a90c8c5595cc5a872bc7')
renter_contract_hash = Hash160Str('0x9cf19e43333a0b4513bd61e2316b40ecb9454a9b')
_ = bytearray(bytes.fromhex(renter_contract_hash.string[2:]))
_.reverse()
print(_)
contract_for_rent_hash = Hash160Str('0xb82bb0da46129f219d657cb6d7fbb22415efc502')