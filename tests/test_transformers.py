from typebuf.transformers import (
    get_transformer_class,
    PythonTransformer,
    TypeScriptTransformer
)

from pytest import raises


def test_get_transformer_class():
    assert get_transformer_class('python') == PythonTransformer
    assert get_transformer_class('typescript') == TypeScriptTransformer

    with raises(Exception):
        get_transformer_class('brainfsck')
