from typing import Any
from boa3.builtin.interop.iterator import Iterator
from boa3.builtin import NeoMetadata, metadata, public
from boa3.builtin.interop.contract import update_contract, call_contract
from boa3.builtin.interop.runtime import executing_script_hash
from boa3.builtin.interop.storage import get, put, find


@metadata
def manifest_metadata() -> NeoMetadata:
    meta = NeoMetadata()
    meta.author = 'github.com/Hecate2'
    meta.description = 'A contract for anyone to deploy his/her own contract temporarily'
    meta.email = 'chenxinhao@ngd.neo.org'
    return meta


@public
def getStorage(key: bytes) -> bytes:
    return get(key)


@public
def findStorage(key: bytes) -> Iterator:
    return find(key)


@public
def putStorage(key: bytes, value: bytes):
    put(key, value)


@public
def anyUpdate0(nef_file: bytes, manifest: bytes, method: str) -> Any:
    update_contract(nef_file, manifest)
    call_result: Any = call_contract(executing_script_hash, method)
    update_contract(get(b'original_nef_file'), get(b'original_manifest'))
    return call_result


@public
def anyUpdate1(nef_file: bytes, manifest: bytes, method: str,
               arg1: Any) -> Any:
    update_contract(nef_file, manifest)
    call_result: Any = call_contract(executing_script_hash, method, [arg1])
    update_contract(get(b'original_nef_file'), get(b'original_manifest'))
    return call_result


@public
def anyUpdate2(nef_file: bytes, manifest: bytes, method: str,
               arg1: Any, arg2: Any) -> Any:
    update_contract(nef_file, manifest)
    call_result: Any = call_contract(executing_script_hash, method, [arg1, arg2])
    update_contract(get(b'original_nef_file'), get(b'original_manifest'))
    return call_result


@public
def anyUpdate3(nef_file: bytes, manifest: bytes, method: str,
               arg1: Any, arg2: Any, arg3: Any) -> Any:
    update_contract(nef_file, manifest)
    call_result: Any = call_contract(executing_script_hash, method, [arg1, arg2, arg3])
    update_contract(get(b'original_nef_file'), get(b'original_manifest'))
    return call_result


@public
def anyUpdate4(nef_file: bytes, manifest: bytes, method: str,
               arg1: Any, arg2: Any, arg3: Any, arg4: Any) -> Any:
    update_contract(nef_file, manifest)
    call_result: Any = call_contract(executing_script_hash, method, [arg1, arg2, arg3, arg4])
    update_contract(get(b'original_nef_file'), get(b'original_manifest'))
    return call_result


@public
def anyUpdate5(nef_file: bytes, manifest: bytes, method: str,
               arg1: Any, arg2: Any, arg3: Any, arg4: Any, arg5: Any) -> Any:
    update_contract(nef_file, manifest)
    call_result: Any = call_contract(executing_script_hash, method, [arg1, arg2, arg3, arg4, arg5])
    update_contract(get(b'original_nef_file'), get(b'original_manifest'))
    return call_result


@public
def anyUpdate6(nef_file: bytes, manifest: bytes, method: str,
               arg1: Any, arg2: Any, arg3: Any, arg4: Any, arg5: Any, arg6: Any) -> Any:
    update_contract(nef_file, manifest)
    call_result: Any = call_contract(executing_script_hash, method, [arg1, arg2, arg3, arg4, arg5, arg6])
    update_contract(get(b'original_nef_file'), get(b'original_manifest'))
    return call_result


@public
def anyUpdate7(nef_file: bytes, manifest: bytes, method: str,
               arg1: Any, arg2: Any, arg3: Any, arg4: Any, arg5: Any, arg6: Any, arg7: Any) -> Any:
    update_contract(nef_file, manifest)
    call_result: Any = call_contract(executing_script_hash, method, [arg1, arg2, arg3, arg4, arg5, arg6, arg7])
    update_contract(get(b'original_nef_file'), get(b'original_manifest'))
    return call_result


@public
def _deploy(data: Any, update: bool):
    put(b'original_nef_file', b'''NEF3neo3-boa by COZ-0.10.0.0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfd\t\x06W\x00\x01xA\x9b\xf6g\xceA\x92]\xe81J\xd8&\x07E\x0c\x00\xdb(@W\x00\x01\x10xA\x9b\xf6g\xceA\xdf0\xb8\x9a@W\x00\x02yxA\x9b\xf6g\xceA\xe6?\x18\x84@W\x01\x03\x0byx\x13\xc0\x0c\x01\x0f\x0c\x06update\x0c\x14\xfd\xa3\xfaCF\xeaS*%\x8f\xc4\x97\xdd\xad\xdbd7\xc9\xfd\xffAb}[RE\xc2\x1fzA\xdb\xfe\xa8tAb}[Rp\x0b\x0c\x11original_manifestA\x9b\xf6g\xceA\x92]\xe81J\xd8&\x07E\x0c\x00\xdb(\x0c\x11original_nef_fileA\x9b\xf6g\xceA\x92]\xe81J\xd8&\x07E\x0c\x00\xdb(\x13\xc0\x0c\x01\x0f\x0c\x06update\x0c\x14\xfd\xa3\xfaCF\xeaS*%\x8f\xc4\x97\xdd\xad\xdbd7\xc9\xfd\xffAb}[REh@W\x01\x04\x0byx\x13\xc0\x0c\x01\x0f\x0c\x06update\x0c\x14\xfd\xa3\xfaCF\xeaS*%\x8f\xc4\x97\xdd\xad\xdbd7\xc9\xfd\xffAb}[RE{\x11\xc0\x1fzA\xdb\xfe\xa8tAb}[Rp\x0b\x0c\x11original_manifestA\x9b\xf6g\xceA\x92]\xe81J\xd8&\x07E\x0c\x00\xdb(\x0c\x11original_nef_fileA\x9b\xf6g\xceA\x92]\xe81J\xd8&\x07E\x0c\x00\xdb(\x13\xc0\x0c\x01\x0f\x0c\x06update\x0c\x14\xfd\xa3\xfaCF\xeaS*%\x8f\xc4\x97\xdd\xad\xdbd7\xc9\xfd\xffAb}[REh@W\x01\x05\x0byx\x13\xc0\x0c\x01\x0f\x0c\x06update\x0c\x14\xfd\xa3\xfaCF\xeaS*%\x8f\xc4\x97\xdd\xad\xdbd7\xc9\xfd\xffAb}[RE|{\x12\xc0\x1fzA\xdb\xfe\xa8tAb}[Rp\x0b\x0c\x11original_manifestA\x9b\xf6g\xceA\x92]\xe81J\xd8&\x07E\x0c\x00\xdb(\x0c\x11original_nef_fileA\x9b\xf6g\xceA\x92]\xe81J\xd8&\x07E\x0c\x00\xdb(\x13\xc0\x0c\x01\x0f\x0c\x06update\x0c\x14\xfd\xa3\xfaCF\xeaS*%\x8f\xc4\x97\xdd\xad\xdbd7\xc9\xfd\xffAb}[REh@W\x01\x06\x0byx\x13\xc0\x0c\x01\x0f\x0c\x06update\x0c\x14\xfd\xa3\xfaCF\xeaS*%\x8f\xc4\x97\xdd\xad\xdbd7\xc9\xfd\xffAb}[RE}|{\x13\xc0\x1fzA\xdb\xfe\xa8tAb}[Rp\x0b\x0c\x11original_manifestA\x9b\xf6g\xceA\x92]\xe81J\xd8&\x07E\x0c\x00\xdb(\x0c\x11original_nef_fileA\x9b\xf6g\xceA\x92]\xe81J\xd8&\x07E\x0c\x00\xdb(\x13\xc0\x0c\x01\x0f\x0c\x06update\x0c\x14\xfd\xa3\xfaCF\xeaS*%\x8f\xc4\x97\xdd\xad\xdbd7\xc9\xfd\xffAb}[REh@W\x01\x07\x0byx\x13\xc0\x0c\x01\x0f\x0c\x06update\x0c\x14\xfd\xa3\xfaCF\xeaS*%\x8f\xc4\x97\xdd\xad\xdbd7\xc9\xfd\xffAb}[RE~}|{\x14\xc0\x1fzA\xdb\xfe\xa8tAb}[Rp\x0b\x0c\x11original_manifestA\x9b\xf6g\xceA\x92]\xe81J\xd8&\x07E\x0c\x00\xdb(\x0c\x11original_nef_fileA\x9b\xf6g\xceA\x92]\xe81J\xd8&\x07E\x0c\x00\xdb(\x13\xc0\x0c\x01\x0f\x0c\x06update\x0c\x14\xfd\xa3\xfaCF\xeaS*%\x8f\xc4\x97\xdd\xad\xdbd7\xc9\xfd\xffAb}[REh@W\x01\x08\x0byx\x13\xc0\x0c\x01\x0f\x0c\x06update\x0c\x14\xfd\xa3\xfaCF\xeaS*%\x8f\xc4\x97\xdd\xad\xdbd7\xc9\xfd\xffAb}[RE\x7f\x07~}|{\x15\xc0\x1fzA\xdb\xfe\xa8tAb}[Rp\x0b\x0c\x11original_manifestA\x9b\xf6g\xceA\x92]\xe81J\xd8&\x07E\x0c\x00\xdb(\x0c\x11original_nef_fileA\x9b\xf6g\xceA\x92]\xe81J\xd8&\x07E\x0c\x00\xdb(\x13\xc0\x0c\x01\x0f\x0c\x06update\x0c\x14\xfd\xa3\xfaCF\xeaS*%\x8f\xc4\x97\xdd\xad\xdbd7\xc9\xfd\xffAb}[REh@W\x01\t\x0byx\x13\xc0\x0c\x01\x0f\x0c\x06update\x0c\x14\xfd\xa3\xfaCF\xeaS*%\x8f\xc4\x97\xdd\xad\xdbd7\xc9\xfd\xffAb}[RE\x7f\x08\x7f\x07~}|{\x16\xc0\x1fzA\xdb\xfe\xa8tAb}[Rp\x0b\x0c\x11original_manifestA\x9b\xf6g\xceA\x92]\xe81J\xd8&\x07E\x0c\x00\xdb(\x0c\x11original_nef_fileA\x9b\xf6g\xceA\x92]\xe81J\xd8&\x07E\x0c\x00\xdb(\x13\xc0\x0c\x01\x0f\x0c\x06update\x0c\x14\xfd\xa3\xfaCF\xeaS*%\x8f\xc4\x97\xdd\xad\xdbd7\xc9\xfd\xffAb}[REh@W\x01\n\x0byx\x13\xc0\x0c\x01\x0f\x0c\x06update\x0c\x14\xfd\xa3\xfaCF\xeaS*%\x8f\xc4\x97\xdd\xad\xdbd7\xc9\xfd\xffAb}[RE\x7f\t\x7f\x08\x7f\x07~}|{\x17\xc0\x1fzA\xdb\xfe\xa8tAb}[Rp\x0b\x0c\x11original_manifestA\x9b\xf6g\xceA\x92]\xe81J\xd8&\x07E\x0c\x00\xdb(\x0c\x11original_nef_fileA\x9b\xf6g\xceA\x92]\xe81J\xd8&\x07E\x0c\x00\xdb(\x13\xc0\x0c\x01\x0f\x0c\x06update\x0c\x14\xfd\xa3\xfaCF\xeaS*%\x8f\xc4\x97\xdd\xad\xdbd7\xc9\xfd\xffAb}[REh@\xc7\x88\xf5\x15''')
    put(b'original_manifest', b'''{"name":"AnyUpdate","groups":[],"abi":{"methods":[{"name":"getStorage","offset":0,"parameters":[{"name":"key","type":"ByteArray"}],"returntype":"ByteArray","safe":false},{"name":"findStorage","offset":24,"parameters":[{"name":"key","type":"ByteArray"}],"returntype":"InteropInterface","safe":false},{"name":"putStorage","offset":40,"parameters":[{"name":"key","type":"ByteArray"},{"name":"value","type":"ByteArray"}],"returntype":"Void","safe":false},{"name":"anyUpdate0","offset":56,"parameters":[{"name":"nef_file","type":"ByteArray"},{"name":"manifest","type":"ByteArray"},{"name":"method","type":"String"}],"returntype":"Any","safe":false},{"name":"anyUpdate1","offset":237,"parameters":[{"name":"nef_file","type":"ByteArray"},{"name":"manifest","type":"ByteArray"},{"name":"method","type":"String"},{"name":"arg1","type":"Any"}],"returntype":"Any","safe":false},{"name":"anyUpdate2","offset":420,"parameters":[{"name":"nef_file","type":"ByteArray"},{"name":"manifest","type":"ByteArray"},{"name":"method","type":"String"},{"name":"arg1","type":"Any"},{"name":"arg2","type":"Any"}],"returntype":"Any","safe":false},{"name":"anyUpdate3","offset":604,"parameters":[{"name":"nef_file","type":"ByteArray"},{"name":"manifest","type":"ByteArray"},{"name":"method","type":"String"},{"name":"arg1","type":"Any"},{"name":"arg2","type":"Any"},{"name":"arg3","type":"Any"}],"returntype":"Any","safe":false},{"name":"anyUpdate4","offset":789,"parameters":[{"name":"nef_file","type":"ByteArray"},{"name":"manifest","type":"ByteArray"},{"name":"method","type":"String"},{"name":"arg1","type":"Any"},{"name":"arg2","type":"Any"},{"name":"arg3","type":"Any"},{"name":"arg4","type":"Any"}],"returntype":"Any","safe":false},{"name":"anyUpdate5","offset":975,"parameters":[{"name":"nef_file","type":"ByteArray"},{"name":"manifest","type":"ByteArray"},{"name":"method","type":"String"},{"name":"arg1","type":"Any"},{"name":"arg2","type":"Any"},{"name":"arg3","type":"Any"},{"name":"arg4","type":"Any"},{"name":"arg5","type":"Any"}],"returntype":"Any","safe":false},{"name":"anyUpdate6","offset":1163,"parameters":[{"name":"nef_file","type":"ByteArray"},{"name":"manifest","type":"ByteArray"},{"name":"method","type":"String"},{"name":"arg1","type":"Any"},{"name":"arg2","type":"Any"},{"name":"arg3","type":"Any"},{"name":"arg4","type":"Any"},{"name":"arg5","type":"Any"},{"name":"arg6","type":"Any"}],"returntype":"Any","safe":false},{"name":"anyUpdate7","offset":1353,"parameters":[{"name":"nef_file","type":"ByteArray"},{"name":"manifest","type":"ByteArray"},{"name":"method","type":"String"},{"name":"arg1","type":"Any"},{"name":"arg2","type":"Any"},{"name":"arg3","type":"Any"},{"name":"arg4","type":"Any"},{"name":"arg5","type":"Any"},{"name":"arg6","type":"Any"},{"name":"arg7","type":"Any"}],"returntype":"Any","safe":false}],"events":[]},"permissions":[{"contract":"*","methods":"*"}],"trusts":[],"features":{},"supportedstandards":[],"extra":{"Author":"github.com/Hecate2","Email":"chenxinhao@ngd.neo.org","Description":"A contract for anyone to deploy his/her own contract temporarily"}}''')
