from typing import Union

from .python import PythonTransformer
from .python_pydantic import PythonPydanticTransformer
from .typescript import TypeScriptTransformer

TokenT = Union[
    PythonTransformer,
    TypeScriptTransformer,
]


def get_transformer_class(language: str):
    if language.lower() == 'python':
        return PythonTransformer
    if language.lower() == 'typescript':
        return TypeScriptTransformer
    if language.lower() == 'python[pydantic]':
        return PythonPydanticTransformer
    else:
        raise ValueError(
            'No compilation tokens found for programming language [%s]..' % language
        )
