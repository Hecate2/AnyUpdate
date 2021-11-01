from typing import List, Any
from boa3.builtin import NeoMetadata, metadata, public
from boa3.builtin.interop.contract import update_contract, call_contract
from boa3.builtin.interop.runtime import executing_script_hash
from boa3.builtin.interop.storage import get, put


@metadata
def manifest_metadata() -> NeoMetadata:
    meta = NeoMetadata()
    meta.author = 'github.com/Hecate2'
    meta.description = 'A short&safe contract for anyone to deploy his/her own contract temporarily'
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
def anyUpdate(nef_file: bytes, manifest: bytes, method: str,
              args: List[Any]) -> Any:
    original_nef_file: bytes = get(b'original_nef_file')
    original_manifest: bytes = get(b'original_manifest')
    update_contract(nef_file, manifest)
    call_result: Any = call_contract(executing_script_hash, method, args)
    put(b'original_nef_file', original_nef_file)
    put(b'original_manifest', original_manifest)
    update_contract(original_nef_file, original_manifest)
    return call_result


@public
def _deploy(data: Any, update: bool):
    put(b'original_nef_file', b'''NEF3neo3-boa by COZ-0.8.2.0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfdQ\x02W\x00\x01xA\x9b\xf6g\xceA\x92]\xe81J\xd8&\x07E\x0c\x00\xdb(@W\x00\x02x\x0c\x11original_nef_file\x97x\x0c\x11original_manifest\x97\xac&\x14\x0c\x0fKey not allowed:yxA\x9b\xf6g\xceA\xe6?\x18\x84@W\x03\x03\x0c\x11original_nef_fileA\x9b\xf6g\xceA\x92]\xe81J\xd8&\x07E\x0c\x00\xdb(p\x0c\x11original_manifestA\x9b\xf6g\xceA\x92]\xe81J\xd8&\x07E\x0c\x00\xdb(q\x0byx\x13\xc0\x0c\x01\x0f\x0c\x06update\x0c\x14\xfd\xa3\xfaCF\xeaS*%\x8f\xc4\x97\xdd\xad\xdbd7\xc9\xfd\xffAb}[RE\xc2\x1fzA\xdb\xfe\xa8tAb}[Rrh\x0c\x11original_nef_fileA\x9b\xf6g\xceA\xe6?\x18\x84i\x0c\x11original_manifestA\x9b\xf6g\xceA\xe6?\x18\x84\x0bih\x13\xc0\x0c\x01\x0f\x0c\x06update\x0c\x14\xfd\xa3\xfaCF\xeaS*%\x8f\xc4\x97\xdd\xad\xdbd7\xc9\xfd\xffAb}[REj@W\x03\x04\x0c\x11original_nef_fileA\x9b\xf6g\xceA\x92]\xe81J\xd8&\x07E\x0c\x00\xdb(p\x0c\x11original_manifestA\x9b\xf6g\xceA\x92]\xe81J\xd8&\x07E\x0c\x00\xdb(q\x0byx\x13\xc0\x0c\x01\x0f\x0c\x06update\x0c\x14\xfd\xa3\xfaCF\xeaS*%\x8f\xc4\x97\xdd\xad\xdbd7\xc9\xfd\xffAb}[RE{\x1fzA\xdb\xfe\xa8tAb}[Rrh\x0c\x11original_nef_fileA\x9b\xf6g\xceA\xe6?\x18\x84i\x0c\x11original_manifestA\x9b\xf6g\xceA\xe6?\x18\x84\x0bih\x13\xc0\x0c\x01\x0f\x0c\x06update\x0c\x14\xfd\xa3\xfaCF\xeaS*%\x8f\xc4\x97\xdd\xad\xdbd7\xc9\xfd\xffAb}[REj@\xde\x1cT2''')
    put(b'original_manifest', b'''{"name":"AnyUpdateShortSafe","groups":[],"abi":{"methods":[{"name":"getStorage","offset":0,"parameters":[{"name":"key","type":"ByteArray"}],"returntype":"ByteArray","safe":false},{"name":"putStorage","offset":24,"parameters":[{"name":"key","type":"ByteArray"},{"name":"value","type":"ByteArray"}],"returntype":"Void","safe":false},{"name":"anyUpdate0","offset":103,"parameters":[{"name":"nef_file","type":"ByteArray"},{"name":"manifest","type":"ByteArray"},{"name":"method","type":"String"}],"returntype":"Any","safe":false},{"name":"anyUpdate","offset":348,"parameters":[{"name":"nef_file","type":"ByteArray"},{"name":"manifest","type":"ByteArray"},{"name":"method","type":"String"},{"name":"args","type":"Array"}],"returntype":"Any","safe":false}],"events":[]},"permissions":[{"contract":"*","methods":"*"}],"trusts":[],"features":[],"supportedstandards":[],"extra":{"Author":"github.com/Hecate2","Email":"chenxinhao@ngd.neo.org","Description":"A short&safe contract for anyone to deploy his/her own contract temporarily"}}''')
