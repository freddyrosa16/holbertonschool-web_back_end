#!/usr/bin/env python3
""" This function takes a list of int, and floats and return their sum as a float. """
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ This function takes a list of int and float"""
    return sum(mxd_lst)
