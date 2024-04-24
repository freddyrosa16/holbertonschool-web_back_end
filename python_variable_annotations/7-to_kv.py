#!/usr/bin/env python3
""" Takes a string `k` and a number `v`
and returns a tuple with `k` as the first element and the
square of `v` as the second element. """
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ This function takes a string and  a int or float and returns a float. """
    return (k, v**2)
