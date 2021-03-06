from typing import Any
from boa3.builtin import NeoMetadata, metadata, public
from boa3.builtin.interop.storage import put


@metadata
def manifest_metadata() -> NeoMetadata:
    meta = NeoMetadata()
    meta.author = 'github.com/Hecate2'
    meta.description = 'A meaningless contract to be tested for AnyUpdate'
    meta.email = 'chenxinhao@ngd.neo.org'
    return meta


@public
def helloNeo() -> str:
    return "Hello Neo!"


@public
def hello1(arg1: Any) -> Any:
    return arg1


@public
def putNef():
    put(b'original_nef_file', b'NO_NEF')