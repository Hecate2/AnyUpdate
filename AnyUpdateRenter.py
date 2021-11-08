from typing import List, Any, cast
from boa3.builtin.interop.iterator import Iterator
from boa3.builtin import NeoMetadata, metadata, public
from boa3.builtin.interop.contract import GAS, update_contract, call_contract
from boa3.builtin.interop.runtime import time, executing_script_hash, calling_script_hash, check_witness
from boa3.builtin.interop.storage import get, put, find, findoptions, StorageMap, get_context
from boa3.builtin.type import UInt160

context = get_context()

"""
Rent an AnyUpdateSafeForRent contract to enjoy exclusive writing permission!
Storage:
    key    ||       value
address[i]    UInt160 script hash of AnyUpdateSafeForRent contracts
expire[i]     timestamp (millisecond) of the rental expiry of each AnyUpdateSafeForRent contract
owner         UInt160 script hash of the owner of this AnyUpdateRenter
price         amount of GAS (*1e-8) to pay for each millisecond of rental
"""


@metadata
def manifest_metadata() -> NeoMetadata:
    meta = NeoMetadata()
    meta.author = 'github.com/Hecate2'
    meta.description = 'Manager of AnyUpdateSafeRent contracts'
    meta.email = 'chenxinhao@ngd.neo.org'
    return meta


@public
def _deploy(data: Any, _update: bool):
    if not _update:
        put(b'owner', UInt160(b'\xa5\xb7QTKV\xdf\xd22\xe0\xea+\x8e\x0c\x9aG\xa2?\x98\xb1'))
        put(b'price', 1)  # 1*1e-8 GAS per millisecond; 0.864 GAS per day


"""
Owner's methods
"""


@public
def update(script: bytes, manifest: bytes, data: Any):
    assert check_witness(cast(UInt160, get(b'owner')))
    update_contract(script, manifest, data)


@public
def setOwner(new_owner: UInt160):
    owner = cast(UInt160, get(b'owner'))
    assert check_witness(owner)
    put(b'owner', new_owner)


@public
def setPricePerBlock(price: int):
    """
    :param price: how many GAS (1e8) to pay for 1 block
          setting price == 1 means 1*1e-8 GAS per millisecond; 0.864 GAS per day
    """
    assert check_witness(cast(UInt160, get(b'owner')))
    put(b'price', price)


@public
def withdraw(to: UInt160, amount: int):
    """
    Allows to get the GAS fees stored in this contract
    :param to: where to send the GAS to
    :param amount: how much GAS to send
    """
    assert check_witness(cast(UInt160, get(b'owner')))
    assert call_contract(GAS, 'transfer', [executing_script_hash, to, amount, None])


@public
def registerContract(i: int, address: UInt160):
    """
    register a new contract's scripthash to be rented by tenants
    :param i: The key to store this contract.
        Owner should be aware not to overwrite other keys
    :param address: scripthash of AnyUpdateSafeForRent contract.
        The owner of registered AnyUpdateSafeForRent should be this AnyUpdateRenter
    """
    assert check_witness(cast(UInt160, get(b'owner')))
    i_bytes = i.to_bytes()
    StorageMap(context, b'address').put(i_bytes, address)
    StorageMap(context, b'expire').put(i_bytes, 0)


@public
def unregisterContract(i: int):
    assert check_witness(cast(UInt160, get(b'owner')))
    i_bytes = i.to_bytes()
    StorageMap(context, b'address').delete(i_bytes)
    StorageMap(context, b'expire').delete(i_bytes)


"""
Methods for everyone
"""


@public
def readContractExpire() -> Iterator:
    """
    The expiry timestamps of contracts for renting
    """
    return find(b'expire', context)


@public
def readContractAddress() -> Iterator:
    """
    The addresses of contracts for renting
    """
    return find(b'address', context)


@public
def getPricePerBlock() -> int:
    return cast(int, get(b'price'))


"""
Tenant's method
"""


@public
def requestRental(payer: UInt160, tenant: UInt160, rental_time: int, desired_contract_ids: List[int]) -> UInt160:
    """
    The caller of this method pays the rental
    :param payer: who will pay for the rental
    :param tenant: who will be the tenant who can use the rented contract
    :param rental_time: rent for how many milliseconds
    :param desired_contract_ids: which contract ids would you like to rent
        if no contract in this list available, then raise Exception
        leave it [] to allow all contracts
    :return: the contract address assigned to the tenant
    """
    if len(desired_contract_ids) > 0:
        for contract_id in desired_contract_ids:
            key = b'expire' + contract_id.to_bytes()
            expire_time = cast(int, get(key))
            if 0 < expire_time < time:
                assert call_contract(GAS, 'transfer',
                                     [payer, executing_script_hash, cast(int, get(b'price')) * rental_time, None])
                rented_contract = cast(UInt160, StorageMap(context, b'address').get(key))
                new_expire_time = time + rental_time
                StorageMap(context, b'expire').put(key, new_expire_time)
                call_contract(rented_contract, 'setTenant', [tenant, new_expire_time])
                return rented_contract
    else:
        iterator = find(b'expire', context, findoptions.FindOptions.REMOVE_PREFIX)
        while iterator.next():
            expire_time = cast(int, iterator.value[1])
            if expire_time < time:
                assert call_contract(GAS, 'transfer', [payer, executing_script_hash, cast(int, get(b'price')) * rental_time, None])
                key_bytes = cast(bytes, iterator.value[0])
                # key_bytes = key_bytes[6:]  # remove b'expire' at the beginning of the key
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
