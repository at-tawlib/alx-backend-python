#!/usr/bin/env python3
from typing import List
"""
Complex types - mixed list
"""


def sum_mixed_list(mxd_lst: List[int | float]) -> float:
    """returns sum of mixed list of floats and integers"""
    return sum(mxd_lst)
