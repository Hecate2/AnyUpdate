from typing import List, Any, cast
from boa3.builtin.interop.iterator import Iterator
from boa3.builtin import NeoMetadata, metadata, public
from boa3.builtin.interop.contract import update_contract, call_contract
from boa3.builtin.interop.runtime import time, executing_script_hash, check_witness
from boa3.builtin.interop.storage import get, put, find
from boa3.builtin.type import UInt160


"""
Storage:
    key    ||       value
_tenant       who is renting this contract. Can be written by the owner and the tenant
              and even the public (when this contract is not rented by anyone)
              The tenant is allowed to overwrite on this key to assign another tenant
_expire       timestamp (millisecond) of the rental expiry. Can be written by the owner.
              If time > read(b'_expire'), then the rental has expired
              and the contract can be used by the public
_owner        UInt160 script hash of the owner of this AnyUpdateSafeForRent
              Typically it should be the script hash of an AnyUpdateRenter
              Overwriting forbidden
_nef_file     the nef file for the contract to be rolled back. Overwriting forbidden
_manifest     the manifest for the contract to be rolled back. Overwriting forbidden
"""


@metadata
def manifest_metadata() -> NeoMetadata:
    meta = NeoMetadata()
    meta.author = 'github.com/Hecate2'
    meta.description = 'A short&safe contract for anyone to rent and deploy his/her own contract temporarily'
    meta.email = 'chenxinhao@ngd.neo.org'
    return meta


@public
def setTenant(tenant: UInt160, expire_timestamp_millisecond: int):
    assert check_witness(cast(UInt160, get(b'_owner')))
    put(b'_tenant', tenant)
    put(b'_expire', expire_timestamp_millisecond)


@public
def checkTenant():
    if time < cast(int, get(b'_expire')):
        # this contract is being rented by the tenant
        if not check_witness(cast(UInt160, get(b'_tenant'))):
            raise Exception('No witness from tenant')
        # else:
        #     this contract is being called by the tenant
    # else:
    #     this contract is public for anyone to use


@public
def getStorage(key: bytes) -> bytes:
    return get(key)


@public
def findStorage(key: bytes) -> Iterator:
    return find(key)


@public
def putStorage(key: bytes, value: bytes):
    checkTenant()
    if key == b'_nef_file' or key == b'_manifest'\
            or key == b'_owner' or key == b'_expire':
        # b'_tenant' is allowed to be re-written by the current tenant
        # Therefore the tenant can re-assign another tenant with this method
        raise Exception('Key not allowed')
    put(key, value)


@public
def anyUpdate(nef_file: bytes, manifest: bytes, method: str,
              args: List[Any]) -> Any:
    checkTenant()
    _nef_file: bytes = get(b'_nef_file')
    _manifest: bytes = get(b'_manifest')
    _owner: bytes = cast(UInt160, get(b'_owner'))
    _expire: bytes = get(b'_expire')
    update_contract(nef_file, manifest)
    call_result: Any = call_contract(executing_script_hash, method, args)
    put(b'_nef_file', _nef_file)
    put(b'_manifest', _manifest)
    put(b'_owner', _owner)
    put(b'_expire', _expire)
    update_contract(_nef_file, _manifest)
    return call_result


@public
def anyUpdate0(nef_file: bytes, manifest: bytes, method: str) -> Any:
    checkTenant()
    _nef_file: bytes = get(b'_nef_file')
    _manifest: bytes = get(b'_manifest')
    _owner: bytes = cast(UInt160, get(b'_owner'))
    _expire: bytes = get(b'_expire')
    update_contract(nef_file, manifest)
    call_result: Any = call_contract(executing_script_hash, method)
    put(b'_nef_file', _nef_file)
    put(b'_manifest', _manifest)
    put(b'_owner', _owner)
    put(b'_expire', _expire)
    update_contract(_nef_file, _manifest)
    return call_result


@public
def _deploy(data: Any, update: bool):
    put(b'_owner', UInt160(b'\x9bJE\xb9\xec@k1\xe2a\xbd\x13E\x0b:3C\x9e\xf1\x9c'))
    # put(b'_tenant', b'''''')
    # put(b'_expire', current_time)
    put(b'_nef_file', b'''NEF3neo3-boa by COZ-0.10.0.0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfd\xa6\x03W\x00\x02\x0c\x06_ownerA\x9b\xf6g\xceA\x92]\xe81J\xd8&\x07E\x0c\x00\xdb(A\xf8'\xec\x8c9x\x0c\x07_tenantA\x9b\xf6g\xceA\xe6?\x18\x84y\x0c\x07_expireA\x9b\xf6g\xceA\xe6?\x18\x84@A\xb7\xc3\x88\x03\x0c\x07_expireA\x9b\xf6g\xceA\x92]\xe81J\xd8&\x07E\x0c\x00\xdb(\xb5&?\x0c\x07_tenantA\x9b\xf6g\xceA\x92]\xe81J\xd8&\x07E\x0c\x00\xdb(A\xf8'\xec\x8c\xaa&\x1b\x0c\x16No witness from tenant:@W\x00\x01xA\x9b\xf6g\xceA\x92]\xe81J\xd8&\x07E\x0c\x00\xdb(@W\x00\x01\x10xA\x9b\xf6g\xceA\xdf0\xb8\x9a@W\x00\x025s\xff\xff\xffx\x0c\t_nef_file\x97x\x0c\t_manifest\x97\xacx\x0c\x06_owner\x97\xacx\x0c\x07_expire\x97\xac&\x14\x0c\x0fKey not allowed:yxA\x9b\xf6g\xceA\xe6?\x18\x84@W\x05\x045\x18\xff\xff\xff\x0c\t_nef_fileA\x9b\xf6g\xceA\x92]\xe81J\xd8&\x07E\x0c\x00\xdb(p\x0c\t_manifestA\x9b\xf6g\xceA\x92]\xe81J\xd8&\x07E\x0c\x00\xdb(q\x0c\x06_ownerA\x9b\xf6g\xceA\x92]\xe81J\xd8&\x07E\x0c\x00\xdb(r\x0c\x07_expireA\x9b\xf6g\xceA\x92]\xe81J\xd8&\x07E\x0c\x00\xdb(s\x0byx\x13\xc0\x0c\x01\x0f\x0c\x06update\x0c\x14\xfd\xa3\xfaCF\xeaS*%\x8f\xc4\x97\xdd\xad\xdbd7\xc9\xfd\xffAb}[RE{\x1fzA\xdb\xfe\xa8tAb}[Rth\x0c\t_nef_fileA\x9b\xf6g\xceA\xe6?\x18\x84i\x0c\t_manifestA\x9b\xf6g\xceA\xe6?\x18\x84j\x0c\x06_ownerA\x9b\xf6g\xceA\xe6?\x18\x84k\x0c\x07_expireA\x9b\xf6g\xceA\xe6?\x18\x84\x0bih\x13\xc0\x0c\x01\x0f\x0c\x06update\x0c\x14\xfd\xa3\xfaCF\xeaS*%\x8f\xc4\x97\xdd\xad\xdbd7\xc9\xfd\xffAb}[REl@W\x05\x035\xde\xfd\xff\xff\x0c\t_nef_fileA\x9b\xf6g\xceA\x92]\xe81J\xd8&\x07E\x0c\x00\xdb(p\x0c\t_manifestA\x9b\xf6g\xceA\x92]\xe81J\xd8&\x07E\x0c\x00\xdb(q\x0c\x06_ownerA\x9b\xf6g\xceA\x92]\xe81J\xd8&\x07E\x0c\x00\xdb(r\x0c\x07_expireA\x9b\xf6g\xceA\x92]\xe81J\xd8&\x07E\x0c\x00\xdb(s\x0byx\x13\xc0\x0c\x01\x0f\x0c\x06update\x0c\x14\xfd\xa3\xfaCF\xeaS*%\x8f\xc4\x97\xdd\xad\xdbd7\xc9\xfd\xffAb}[RE\xc2\x1fzA\xdb\xfe\xa8tAb}[Rth\x0c\t_nef_fileA\x9b\xf6g\xceA\xe6?\x18\x84i\x0c\t_manifestA\x9b\xf6g\xceA\xe6?\x18\x84j\x0c\x06_ownerA\x9b\xf6g\xceA\xe6?\x18\x84k\x0c\x07_expireA\x9b\xf6g\xceA\xe6?\x18\x84\x0bih\x13\xc0\x0c\x01\x0f\x0c\x06update\x0c\x14\xfd\xa3\xfaCF\xeaS*%\x8f\xc4\x97\xdd\xad\xdbd7\xc9\xfd\xffAb}[REl@\x80,\xfa\xfb''')
    put(b'_manifest', b'''{"name":"AnyUpdateSafeForRent","groups":[],"abi":{"methods":[{"name":"setTenant","offset":0,"parameters":[{"name":"tenant","type":"Hash160"},{"name":"expire_timestamp_millisecond","type":"Integer"}],"returntype":"Void","safe":false},{"name":"checkTenant","offset":77,"parameters":[],"returntype":"Void","safe":false},{"name":"getStorage","offset":175,"parameters":[{"name":"key","type":"ByteArray"}],"returntype":"ByteArray","safe":false},{"name":"findStorage","offset":199,"parameters":[{"name":"key","type":"ByteArray"}],"returntype":"InteropInterface","safe":false},{"name":"putStorage","offset":215,"parameters":[{"name":"key","type":"ByteArray"},{"name":"value","type":"ByteArray"}],"returntype":"Void","safe":false},{"name":"anyUpdate","offset":306,"parameters":[{"name":"nef_file","type":"ByteArray"},{"name":"manifest","type":"ByteArray"},{"name":"method","type":"String"},{"name":"args","type":"Array"}],"returntype":"Any","safe":false},{"name":"anyUpdate0","offset":620,"parameters":[{"name":"nef_file","type":"ByteArray"},{"name":"manifest","type":"ByteArray"},{"name":"method","type":"String"}],"returntype":"Any","safe":false}],"events":[]},"permissions":[{"contract":"*","methods":"*"}],"trusts":[],"features":{},"supportedstandards":[],"extra":{"Author":"github.com/Hecate2","Email":"chenxinhao@ngd.neo.org","Description":"A short&safe contract for anyone to rent and deploy his/her own contract temporarily"}}''')
