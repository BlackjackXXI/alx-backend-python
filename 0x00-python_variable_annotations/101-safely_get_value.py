#!/usr/bin/env python3
"""Module for a type-annotated function safely_get_value."""

from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')

def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    """Return the value for a key in a dictionary or a default value."""
    if key in dct:
        return dct[key]
    else:
        return default
