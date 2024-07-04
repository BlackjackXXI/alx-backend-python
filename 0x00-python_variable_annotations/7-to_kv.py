#!/usr/bin/env python3
"""Module for a type-annotated function to_kv."""

from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple with a string and the square of the int/float."""
    return (k, float(v**2))
