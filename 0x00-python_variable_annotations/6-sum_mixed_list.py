#!/usr/bin/env python3
"""
Complex types - mixed list
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int,float]]) -> float:
    """returns sum of mixed list of floats and integers"""
    return float(sum(mxd_lst))
