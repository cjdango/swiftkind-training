import math
from random import random


def add_int(a, b):
    """
    Adds two num and return as integer
    """
    return int(a + b)


def sub_float(a, b):
    """
    Subtract two num and return as float num
    """
    return float(a - b)


def mult_complex(a, b):
    """
    Multiply two num and return as complex num
    """
    return complex(a * b)


def div_abs(a, b):
    """
    Divide two num then return as absolute
    """
    return math.fabs(a / b)


def add_two_sqrt(num):
    """
    Add 2 to num then return its sqrt
    """
    return math.sqrt(num + 2)


def sub_two_ceil(num):
    """
    Subtract 2 from num then return its ceil
    """
    return math.ceil(num - 2)


def mult_two_floor(num):
    """
    Multiply 2 and num then return its floor
    """
    return math.floor(num * 2)


def get_sin_plus_two(num):
    """
    Return the sine of x radians then add two.
    """
    return math.sin(num + 2)


def get_rand_plus_two():
    """
    Return random number and add two
    """
    return random() + 2


def get_pi_plus_two():
    """
    Return pi and add two
    """
    return math.pi + 2


print('add_int', add_int(1.3, 2))
print('sub_float', sub_float(4, 2))
print('mult_complex', mult_complex(4, 2))
print('div_abs', div_abs(2, 4))
print('add_two_sqrt', add_two_sqrt(8))
print('sub_two_ceil', sub_two_ceil(5.8))
print('mult_two_floor', mult_two_floor(5.8))
print('get_sin_plus_two', get_sin_plus_two(24))
print('get_rand_plus_two', get_rand_plus_two())
print('get_pi_plus_two', get_pi_plus_two())
