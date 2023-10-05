#!/usr/bin/env python3
''' Description: Accepts float multiplier as argument and returns a function
                 that multiplies a float by multiplier
'''

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    ''' Creates a multiplier function. '''
    return lambda x: x * multiplier
