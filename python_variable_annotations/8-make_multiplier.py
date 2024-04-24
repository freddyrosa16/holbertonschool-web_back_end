#!/usr/bin/env python3
"""Returns a function that multiplies a given number by the specified multiplier."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ This function takes a float as argument and returns a function that multiplies a float. """
    def mult(n: float) -> float:
        """ This function takes a float and multiply. """
        return n * multiplier
    return mult
