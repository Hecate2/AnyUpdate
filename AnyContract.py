from boa3.builtin import NeoMetadata, metadata, public


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
