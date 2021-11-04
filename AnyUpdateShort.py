from typing import List, Any
from boa3.builtin.interop.iterator import Iterator
from boa3.builtin import NeoMetadata, metadata, public
from boa3.builtin.interop.contract import update_contract, call_contract
from boa3.builtin.interop.runtime import executing_script_hash
from boa3.builtin.interop.storage import get, put, find
from boa3.builtin.type import UInt160


@metadata
def manifest_metadata() -> NeoMetadata:
    meta = NeoMetadata()
    meta.author = 'github.com/Hecate2'
    meta.description = 'A short contract for anyone to deploy his/her own contract temporarily'
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
def anyUpdate(nef_file: bytes, manifest: bytes, method: str,
              args: List[Any]) -> Any:
    update_contract(nef_file, manifest)
    call_result: Any = call_contract(executing_script_hash, method, args)
    update_contract(get(b'original_nef_file'), get(b'original_manifest'))
    return call_result


@public
def updateAndCallAnother(nef_file: bytes, manifest: bytes,
                         another_contract: UInt160, method: str, args: List[Any]) -> Any:
    update_contract(nef_file, manifest)
    call_result: Any = call_contract(another_contract, method, args)
    update_contract(get(b'original_nef_file'), get(b'original_manifest'))
    return call_result


@public
def _deploy(data: Any, update: bool):
    put(b'original_nef_file', b'''NEF3neo3-boa by COZ-0.10.0.0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfdS\x02W\x00\x01xA\x9b\xf6g\xceA\x92]\xe81J\xd8&\x07E\x0c\x00\xdb(@W\x00\x01\x10xA\x9b\xf6g\xceA\xdf0\xb8\x9a@W\x00\x02yxA\x9b\xf6g\xceA\xe6?\x18\x84@W\x01\x03\x0byx\x13\xc0\x0c\x01\x0f\x0c\x06update\x0c\x14\xfd\xa3\xfaCF\xeaS*%\x8f\xc4\x97\xdd\xad\xdbd7\xc9\xfd\xffAb}[RE\xc2\x1fzA\xdb\xfe\xa8tAb}[Rp\x0b\x0c\x11original_manifestA\x9b\xf6g\xceA\x92]\xe81J\xd8&\x07E\x0c\x00\xdb(\x0c\x11original_nef_fileA\x9b\xf6g\xceA\x92]\xe81J\xd8&\x07E\x0c\x00\xdb(\x13\xc0\x0c\x01\x0f\x0c\x06update\x0c\x14\xfd\xa3\xfaCF\xeaS*%\x8f\xc4\x97\xdd\xad\xdbd7\xc9\xfd\xffAb}[REh@W\x01\x04\x0byx\x13\xc0\x0c\x01\x0f\x0c\x06update\x0c\x14\xfd\xa3\xfaCF\xeaS*%\x8f\xc4\x97\xdd\xad\xdbd7\xc9\xfd\xffAb}[RE{\x1fzA\xdb\xfe\xa8tAb}[Rp\x0b\x0c\x11original_manifestA\x9b\xf6g\xceA\x92]\xe81J\xd8&\x07E\x0c\x00\xdb(\x0c\x11original_nef_fileA\x9b\xf6g\xceA\x92]\xe81J\xd8&\x07E\x0c\x00\xdb(\x13\xc0\x0c\x01\x0f\x0c\x06update\x0c\x14\xfd\xa3\xfaCF\xeaS*%\x8f\xc4\x97\xdd\xad\xdbd7\xc9\xfd\xffAb}[REh@W\x01\x05\x0byx\x13\xc0\x0c\x01\x0f\x0c\x06update\x0c\x14\xfd\xa3\xfaCF\xeaS*%\x8f\xc4\x97\xdd\xad\xdbd7\xc9\xfd\xffAb}[RE|\x1f{zAb}[Rp\x0b\x0c\x11original_manifestA\x9b\xf6g\xceA\x92]\xe81J\xd8&\x07E\x0c\x00\xdb(\x0c\x11original_nef_fileA\x9b\xf6g\xceA\x92]\xe81J\xd8&\x07E\x0c\x00\xdb(\x13\xc0\x0c\x01\x0f\x0c\x06update\x0c\x14\xfd\xa3\xfaCF\xeaS*%\x8f\xc4\x97\xdd\xad\xdbd7\xc9\xfd\xffAb}[REh@?\x89y\x1b''')
    put(b'original_manifest', b'''{"name":"AnyUpdateShort","groups":[],"abi":{"methods":[{"name":"getStorage","offset":0,"parameters":[{"name":"key","type":"ByteArray"}],"returntype":"ByteArray","safe":false},{"name":"findStorage","offset":24,"parameters":[{"name":"key","type":"ByteArray"}],"returntype":"InteropInterface","safe":false},{"name":"putStorage","offset":40,"parameters":[{"name":"key","type":"ByteArray"},{"name":"value","type":"ByteArray"}],"returntype":"Void","safe":false},{"name":"anyUpdate0","offset":56,"parameters":[{"name":"nef_file","type":"ByteArray"},{"name":"manifest","type":"ByteArray"},{"name":"method","type":"String"}],"returntype":"Any","safe":false},{"name":"anyUpdate","offset":237,"parameters":[{"name":"nef_file","type":"ByteArray"},{"name":"manifest","type":"ByteArray"},{"name":"method","type":"String"},{"name":"args","type":"Array"}],"returntype":"Any","safe":false},{"name":"updateAndCallAnother","offset":418,"parameters":[{"name":"nef_file","type":"ByteArray"},{"name":"manifest","type":"ByteArray"},{"name":"another_contract","type":"Hash160"},{"name":"method","type":"String"},{"name":"args","type":"Array"}],"returntype":"Any","safe":false}],"events":[]},"permissions":[{"contract":"*","methods":"*"}],"trusts":[],"features":{},"supportedstandards":[],"extra":{"Author":"github.com/Hecate2","Email":"chenxinhao@ngd.neo.org","Description":"A short contract for anyone to deploy his/her own contract temporarily"}}''')
