from typing import Any
from boa3.builtin import NeoMetadata, metadata, public
from boa3.builtin.interop.contract import update_contract, call_contract
from boa3.builtin.interop.runtime import executing_script_hash
from boa3.builtin.interop.storage import get, put


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
def putStorage(key: bytes, value: bytes):
    if key == b'original_nef_file' or key == b'original_manifest':
        raise Exception('Key not allowed')
    put(key, value)


@public
def anyUpdate0(nef_file: bytes, manifest: bytes, method: str) -> Any:
    original_nef_file: bytes = get(b'original_nef_file')
    original_manifest: bytes = get(b'original_manifest')
    update_contract(nef_file, manifest)
    call_result: Any = call_contract(executing_script_hash, method)
    put(b'original_nef_file', original_nef_file)
    put(b'original_manifest', original_manifest)
    update_contract(original_nef_file, original_manifest)
    return call_result


@public
def anyUpdate1(nef_file: bytes, manifest: bytes, method: str,
               arg1: Any) -> Any:
    original_nef_file: bytes = get(b'original_nef_file')
    original_manifest: bytes = get(b'original_manifest')
    update_contract(nef_file, manifest)
    call_result: Any = call_contract(executing_script_hash, method, [arg1])
    put(b'original_nef_file', original_nef_file)
    put(b'original_manifest', original_manifest)
    update_contract(original_nef_file, original_manifest)
    return call_result


@public
def anyUpdate2(nef_file: bytes, manifest: bytes, method: str,
               arg1: Any, arg2: Any) -> Any:
    original_nef_file: bytes = get(b'original_nef_file')
    original_manifest: bytes = get(b'original_manifest')
    update_contract(nef_file, manifest)
    call_result: Any = call_contract(executing_script_hash, method, [arg1, arg2])
    put(b'original_nef_file', original_nef_file)
    put(b'original_manifest', original_manifest)
    update_contract(original_nef_file, original_manifest)
    return call_result


@public
def anyUpdate3(nef_file: bytes, manifest: bytes, method: str,
               arg1: Any, arg2: Any, arg3: Any) -> Any:
    original_nef_file: bytes = get(b'original_nef_file')
    original_manifest: bytes = get(b'original_manifest')
    update_contract(nef_file, manifest)
    call_result: Any = call_contract(executing_script_hash, method, [arg1, arg2, arg3])
    put(b'original_nef_file', original_nef_file)
    put(b'original_manifest', original_manifest)
    update_contract(original_nef_file, original_manifest)
    return call_result


@public
def anyUpdate4(nef_file: bytes, manifest: bytes, method: str,
               arg1: Any, arg2: Any, arg3: Any, arg4: Any) -> Any:
    original_nef_file: bytes = get(b'original_nef_file')
    original_manifest: bytes = get(b'original_manifest')
    update_contract(nef_file, manifest)
    call_result: Any = call_contract(executing_script_hash, method, [arg1, arg2, arg3, arg4])
    put(b'original_nef_file', original_nef_file)
    put(b'original_manifest', original_manifest)
    update_contract(original_nef_file, original_manifest)
    return call_result


@public
def anyUpdate5(nef_file: bytes, manifest: bytes, method: str,
               arg1: Any, arg2: Any, arg3: Any, arg4: Any, arg5: Any) -> Any:
    original_nef_file: bytes = get(b'original_nef_file')
    original_manifest: bytes = get(b'original_manifest')
    update_contract(nef_file, manifest)
    call_result: Any = call_contract(executing_script_hash, method, [arg1, arg2, arg3, arg4, arg5])
    put(b'original_nef_file', original_nef_file)
    put(b'original_manifest', original_manifest)
    update_contract(original_nef_file, original_manifest)
    return call_result


@public
def anyUpdate6(nef_file: bytes, manifest: bytes, method: str,
               arg1: Any, arg2: Any, arg3: Any, arg4: Any, arg5: Any, arg6: Any) -> Any:
    original_nef_file: bytes = get(b'original_nef_file')
    original_manifest: bytes = get(b'original_manifest')
    update_contract(nef_file, manifest)
    call_result: Any = call_contract(executing_script_hash, method, [arg1, arg2, arg3, arg4, arg5, arg6])
    put(b'original_nef_file', original_nef_file)
    put(b'original_manifest', original_manifest)
    update_contract(original_nef_file, original_manifest)
    return call_result


@public
def anyUpdate7(nef_file: bytes, manifest: bytes, method: str,
               arg1: Any, arg2: Any, arg3: Any, arg4: Any, arg5: Any, arg6: Any, arg7: Any) -> Any:
    original_nef_file: bytes = get(b'original_nef_file')
    original_manifest: bytes = get(b'original_manifest')
    update_contract(nef_file, manifest)
    call_result: Any = call_contract(executing_script_hash, method, [arg1, arg2, arg3, arg4, arg5, arg6, arg7])
    put(b'original_nef_file', original_nef_file)
    put(b'original_manifest', original_manifest)
    update_contract(original_nef_file, original_manifest)
    return call_result


@public
def _deploy(data: Any, update: bool):
    put(b'original_nef_file', b'''NEF3neo3-boa by COZ-0.8.2.0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfd8\x08W\x00\x01xA\x9b\xf6g\xceA\x92]\xe81J\xd8&\x07E\x0c\x00\xdb(@W\x00\x02x\x0c\x11original_nef_file\x97x\x0c\x11original_manifest\x97\xac&\x14\x0c\x0fKey not allowed:yxA\x9b\xf6g\xceA\xe6?\x18\x84@W\x03\x03\x0c\x11original_nef_fileA\x9b\xf6g\xceA\x92]\xe81J\xd8&\x07E\x0c\x00\xdb(p\x0c\x11original_manifestA\x9b\xf6g\xceA\x92]\xe81J\xd8&\x07E\x0c\x00\xdb(q\x0byx\x13\xc0\x0c\x01\x0f\x0c\x06update\x0c\x14\xfd\xa3\xfaCF\xeaS*%\x8f\xc4\x97\xdd\xad\xdbd7\xc9\xfd\xffAb}[RE\xc2\x1fzA\xdb\xfe\xa8tAb}[Rrh\x0c\x11original_nef_fileA\x9b\xf6g\xceA\xe6?\x18\x84i\x0c\x11original_manifestA\x9b\xf6g\xceA\xe6?\x18\x84\x0bih\x13\xc0\x0c\x01\x0f\x0c\x06update\x0c\x14\xfd\xa3\xfaCF\xeaS*%\x8f\xc4\x97\xdd\xad\xdbd7\xc9\xfd\xffAb}[REj@W\x03\x04\x0c\x11original_nef_fileA\x9b\xf6g\xceA\x92]\xe81J\xd8&\x07E\x0c\x00\xdb(p\x0c\x11original_manifestA\x9b\xf6g\xceA\x92]\xe81J\xd8&\x07E\x0c\x00\xdb(q\x0byx\x13\xc0\x0c\x01\x0f\x0c\x06update\x0c\x14\xfd\xa3\xfaCF\xeaS*%\x8f\xc4\x97\xdd\xad\xdbd7\xc9\xfd\xffAb}[RE{\x11\xc0\x1fzA\xdb\xfe\xa8tAb}[Rrh\x0c\x11original_nef_fileA\x9b\xf6g\xceA\xe6?\x18\x84i\x0c\x11original_manifestA\x9b\xf6g\xceA\xe6?\x18\x84\x0bih\x13\xc0\x0c\x01\x0f\x0c\x06update\x0c\x14\xfd\xa3\xfaCF\xeaS*%\x8f\xc4\x97\xdd\xad\xdbd7\xc9\xfd\xffAb}[REj@W\x03\x05\x0c\x11original_nef_fileA\x9b\xf6g\xceA\x92]\xe81J\xd8&\x07E\x0c\x00\xdb(p\x0c\x11original_manifestA\x9b\xf6g\xceA\x92]\xe81J\xd8&\x07E\x0c\x00\xdb(q\x0byx\x13\xc0\x0c\x01\x0f\x0c\x06update\x0c\x14\xfd\xa3\xfaCF\xeaS*%\x8f\xc4\x97\xdd\xad\xdbd7\xc9\xfd\xffAb}[RE|{\x12\xc0\x1fzA\xdb\xfe\xa8tAb}[Rrh\x0c\x11original_nef_fileA\x9b\xf6g\xceA\xe6?\x18\x84i\x0c\x11original_manifestA\x9b\xf6g\xceA\xe6?\x18\x84\x0bih\x13\xc0\x0c\x01\x0f\x0c\x06update\x0c\x14\xfd\xa3\xfaCF\xeaS*%\x8f\xc4\x97\xdd\xad\xdbd7\xc9\xfd\xffAb}[REj@W\x03\x06\x0c\x11original_nef_fileA\x9b\xf6g\xceA\x92]\xe81J\xd8&\x07E\x0c\x00\xdb(p\x0c\x11original_manifestA\x9b\xf6g\xceA\x92]\xe81J\xd8&\x07E\x0c\x00\xdb(q\x0byx\x13\xc0\x0c\x01\x0f\x0c\x06update\x0c\x14\xfd\xa3\xfaCF\xeaS*%\x8f\xc4\x97\xdd\xad\xdbd7\xc9\xfd\xffAb}[RE}|{\x13\xc0\x1fzA\xdb\xfe\xa8tAb}[Rrh\x0c\x11original_nef_fileA\x9b\xf6g\xceA\xe6?\x18\x84i\x0c\x11original_manifestA\x9b\xf6g\xceA\xe6?\x18\x84\x0bih\x13\xc0\x0c\x01\x0f\x0c\x06update\x0c\x14\xfd\xa3\xfaCF\xeaS*%\x8f\xc4\x97\xdd\xad\xdbd7\xc9\xfd\xffAb}[REj@W\x03\x07\x0c\x11original_nef_fileA\x9b\xf6g\xceA\x92]\xe81J\xd8&\x07E\x0c\x00\xdb(p\x0c\x11original_manifestA\x9b\xf6g\xceA\x92]\xe81J\xd8&\x07E\x0c\x00\xdb(q\x0byx\x13\xc0\x0c\x01\x0f\x0c\x06update\x0c\x14\xfd\xa3\xfaCF\xeaS*%\x8f\xc4\x97\xdd\xad\xdbd7\xc9\xfd\xffAb}[RE~}|{\x14\xc0\x1fzA\xdb\xfe\xa8tAb}[Rrh\x0c\x11original_nef_fileA\x9b\xf6g\xceA\xe6?\x18\x84i\x0c\x11original_manifestA\x9b\xf6g\xceA\xe6?\x18\x84\x0bih\x13\xc0\x0c\x01\x0f\x0c\x06update\x0c\x14\xfd\xa3\xfaCF\xeaS*%\x8f\xc4\x97\xdd\xad\xdbd7\xc9\xfd\xffAb}[REj@W\x03\x08\x0c\x11original_nef_fileA\x9b\xf6g\xceA\x92]\xe81J\xd8&\x07E\x0c\x00\xdb(p\x0c\x11original_manifestA\x9b\xf6g\xceA\x92]\xe81J\xd8&\x07E\x0c\x00\xdb(q\x0byx\x13\xc0\x0c\x01\x0f\x0c\x06update\x0c\x14\xfd\xa3\xfaCF\xeaS*%\x8f\xc4\x97\xdd\xad\xdbd7\xc9\xfd\xffAb}[RE\x7f\x07~}|{\x15\xc0\x1fzA\xdb\xfe\xa8tAb}[Rrh\x0c\x11original_nef_fileA\x9b\xf6g\xceA\xe6?\x18\x84i\x0c\x11original_manifestA\x9b\xf6g\xceA\xe6?\x18\x84\x0bih\x13\xc0\x0c\x01\x0f\x0c\x06update\x0c\x14\xfd\xa3\xfaCF\xeaS*%\x8f\xc4\x97\xdd\xad\xdbd7\xc9\xfd\xffAb}[REj@W\x03\t\x0c\x11original_nef_fileA\x9b\xf6g\xceA\x92]\xe81J\xd8&\x07E\x0c\x00\xdb(p\x0c\x11original_manifestA\x9b\xf6g\xceA\x92]\xe81J\xd8&\x07E\x0c\x00\xdb(q\x0byx\x13\xc0\x0c\x01\x0f\x0c\x06update\x0c\x14\xfd\xa3\xfaCF\xeaS*%\x8f\xc4\x97\xdd\xad\xdbd7\xc9\xfd\xffAb}[RE\x7f\x08\x7f\x07~}|{\x16\xc0\x1fzA\xdb\xfe\xa8tAb}[Rrh\x0c\x11original_nef_fileA\x9b\xf6g\xceA\xe6?\x18\x84i\x0c\x11original_manifestA\x9b\xf6g\xceA\xe6?\x18\x84\x0bih\x13\xc0\x0c\x01\x0f\x0c\x06update\x0c\x14\xfd\xa3\xfaCF\xeaS*%\x8f\xc4\x97\xdd\xad\xdbd7\xc9\xfd\xffAb}[REj@W\x03\n\x0c\x11original_nef_fileA\x9b\xf6g\xceA\x92]\xe81J\xd8&\x07E\x0c\x00\xdb(p\x0c\x11original_manifestA\x9b\xf6g\xceA\x92]\xe81J\xd8&\x07E\x0c\x00\xdb(q\x0byx\x13\xc0\x0c\x01\x0f\x0c\x06update\x0c\x14\xfd\xa3\xfaCF\xeaS*%\x8f\xc4\x97\xdd\xad\xdbd7\xc9\xfd\xffAb}[RE\x7f\t\x7f\x08\x7f\x07~}|{\x17\xc0\x1fzA\xdb\xfe\xa8tAb}[Rrh\x0c\x11original_nef_fileA\x9b\xf6g\xceA\xe6?\x18\x84i\x0c\x11original_manifestA\x9b\xf6g\xceA\xe6?\x18\x84\x0bih\x13\xc0\x0c\x01\x0f\x0c\x06update\x0c\x14\xfd\xa3\xfaCF\xeaS*%\x8f\xc4\x97\xdd\xad\xdbd7\xc9\xfd\xffAb}[REj@(\x06\xfd\x87''')
    put(b'original_manifest', b'''{"name":"AnyUpdateSafe","groups":[],"abi":{"methods":[{"name":"getStorage","offset":0,"parameters":[{"name":"key","type":"ByteArray"}],"returntype":"ByteArray","safe":false},{"name":"putStorage","offset":24,"parameters":[{"name":"key","type":"ByteArray"},{"name":"value","type":"ByteArray"}],"returntype":"Void","safe":false},{"name":"anyUpdate0","offset":103,"parameters":[{"name":"nef_file","type":"ByteArray"},{"name":"manifest","type":"ByteArray"},{"name":"method","type":"String"}],"returntype":"Any","safe":false},{"name":"anyUpdate1","offset":348,"parameters":[{"name":"nef_file","type":"ByteArray"},{"name":"manifest","type":"ByteArray"},{"name":"method","type":"String"},{"name":"arg1","type":"Any"}],"returntype":"Any","safe":false},{"name":"anyUpdate2","offset":595,"parameters":[{"name":"nef_file","type":"ByteArray"},{"name":"manifest","type":"ByteArray"},{"name":"method","type":"String"},{"name":"arg1","type":"Any"},{"name":"arg2","type":"Any"}],"returntype":"Any","safe":false},{"name":"anyUpdate3","offset":843,"parameters":[{"name":"nef_file","type":"ByteArray"},{"name":"manifest","type":"ByteArray"},{"name":"method","type":"String"},{"name":"arg1","type":"Any"},{"name":"arg2","type":"Any"},{"name":"arg3","type":"Any"}],"returntype":"Any","safe":false},{"name":"anyUpdate4","offset":1092,"parameters":[{"name":"nef_file","type":"ByteArray"},{"name":"manifest","type":"ByteArray"},{"name":"method","type":"String"},{"name":"arg1","type":"Any"},{"name":"arg2","type":"Any"},{"name":"arg3","type":"Any"},{"name":"arg4","type":"Any"}],"returntype":"Any","safe":false},{"name":"anyUpdate5","offset":1342,"parameters":[{"name":"nef_file","type":"ByteArray"},{"name":"manifest","type":"ByteArray"},{"name":"method","type":"String"},{"name":"arg1","type":"Any"},{"name":"arg2","type":"Any"},{"name":"arg3","type":"Any"},{"name":"arg4","type":"Any"},{"name":"arg5","type":"Any"}],"returntype":"Any","safe":false},{"name":"anyUpdate6","offset":1594,"parameters":[{"name":"nef_file","type":"ByteArray"},{"name":"manifest","type":"ByteArray"},{"name":"method","type":"String"},{"name":"arg1","type":"Any"},{"name":"arg2","type":"Any"},{"name":"arg3","type":"Any"},{"name":"arg4","type":"Any"},{"name":"arg5","type":"Any"},{"name":"arg6","type":"Any"}],"returntype":"Any","safe":false},{"name":"anyUpdate7","offset":1848,"parameters":[{"name":"nef_file","type":"ByteArray"},{"name":"manifest","type":"ByteArray"},{"name":"method","type":"String"},{"name":"arg1","type":"Any"},{"name":"arg2","type":"Any"},{"name":"arg3","type":"Any"},{"name":"arg4","type":"Any"},{"name":"arg5","type":"Any"},{"name":"arg6","type":"Any"},{"name":"arg7","type":"Any"}],"returntype":"Any","safe":false}],"events":[]},"permissions":[{"contract":"*","methods":"*"}],"trusts":[],"features":[],"supportedstandards":[],"extra":{"Author":"github.com/Hecate2","Email":"chenxinhao@ngd.neo.org","Description":"A contract for anyone to deploy his/her own contract temporarily"}}''')
