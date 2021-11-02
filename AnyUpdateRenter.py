from typing import Any, cast
from boa3.builtin.interop.iterator import Iterator
from boa3.builtin import NeoMetadata, metadata, public
from boa3.builtin.interop.contract import GAS, update_contract, call_contract
from boa3.builtin.interop.runtime import time, executing_script_hash, calling_script_hash, check_witness
from boa3.builtin.interop.storage import get, put, find, StorageMap, get_context
from boa3.builtin.type import UInt160


@metadata
def manifest_metadata() -> NeoMetadata:
    meta = NeoMetadata()
    meta.author = 'github.com/Hecate2'
    meta.description = 'Manager of AnyUpdateSafeRent contracts'
    meta.email = 'chenxinhao@ngd.neo.org'
    return meta


"""
Owner's methods
"""


@public
def _deploy(data: Any, _update: bool):
    if not _update:
        put(b'owner', UInt160(b'\xa5\xb7QTKV\xdf\xd22\xe0\xea+\x8e\x0c\x9aG\xa2?\x98\xb1'))
        put(b'price', 1)  # 1*1e-8 GAS per millisecond; 0.864 GAS per day


@public
def setOwner(new_owner: UInt160):
    owner = cast(UInt160, get(b'owner'))
    assert check_witness(owner)
    put(b'owner', new_owner)


@public
def update(script: bytes, manifest: bytes, data: Any):
    assert check_witness(cast(UInt160, get(b'owner')))
    update_contract(script, manifest, data)


@public
def setPricePerBlock(price: int):
    """
    :param price: how many GAS (1e8) to pay for 1 block
    """
    assert check_witness(cast(UInt160, get(b'owner')))
    put(b'price', price)


@public
def withdraw(to: UInt160, amount: int):
    assert check_witness(cast(UInt160, get(b'owner')))
    assert call_contract(GAS, 'transfer', [executing_script_hash, to, amount, None])


@public
def registerContract(i: int, address: UInt160):
    assert check_witness(cast(UInt160, get(b'owner')))
    context = get_context()
    i_bytes = i.to_bytes()
    StorageMap(context, b'address').put(i_bytes, address)
    StorageMap(context, b'expire').put(i_bytes, 0)


@public
def unregisterContract(i: int):
    assert check_witness(cast(UInt160, get(b'owner')))
    context = get_context()
    i_bytes = i.to_bytes()
    StorageMap(context, b'address').delete(i_bytes)
    StorageMap(context, b'expire').delete(i_bytes)


"""
Methods for everyone
"""


@public
def readContractExpire() -> Iterator:
    return find(b'expire', get_context())


@public
def readContractAddress() -> Iterator:
    return find(b'address', get_context())


@public
def getPricePerBlock() -> int:
    return cast(int, get(b'price'))


"""
Tenant's method
"""


@public
def requestRental(payer: UInt160, tenant: UInt160, rental_time: int) -> UInt160:
    """
    The caller of this method pays the rental
    :param payer: who will pay for the rental
    :param tenant: who will be the tenant who can use the rented contract
    :param rental_time: rent for how many milliseconds
    :return: the contract address assigned to the tenant
    """
    iterator = find(b'expire')
    while iterator.next():
        expire_time = cast(bytes, iterator.value[1]).to_int()
        if expire_time < time:
            context = get_context()
            assert call_contract(GAS, 'transfer', [payer, executing_script_hash, cast(int, get(b'price')) * rental_time, None])
            key_bytes = cast(bytes, iterator.value[0])
            key_bytes = key_bytes[6:]  # remove b'expire' at the beginning of the key
            rented_contract = cast(UInt160, StorageMap(context, b'address').get(key_bytes))
            new_expire_time = time + rental_time
            StorageMap(context, b'expire').put(key_bytes, new_expire_time)
            call_contract(rented_contract, 'setTenant', [tenant, new_expire_time])
            return rented_contract
    raise Exception('No contract available')
    return tenant


@public
def onNEP17Payment(from_address: UInt160, amount: int, data: Any):
    if calling_script_hash != GAS:
        raise Exception('Only GAS allowed')
