#!/usr/bin/env python3
"""
Duck typing - first element of a sequence
"""
from typing import Any, Union, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """gets and list and returns the first index"""
    if lst:
        return lst[0]
    else:
        return None
