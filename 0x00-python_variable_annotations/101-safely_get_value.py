#!/usr/bin/env python3
"""
More involved type annotations
"""
from typing import Mapping, Any, Union, TypeVar
T = TypeVar("T")
Def = Union[T, None]
Res = Union[Any, T]


def safely_get_value(dct: Mapping, key: Any, default: Def = None) -> Res:
    """ adding type annotations to the function"""
    if key in dct:
        return dct[key]
    else:
        return default
