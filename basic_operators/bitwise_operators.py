def binary_and(a, b):
    """
    Copies a bit to the result if it exists in both operands
    """
    return a & b


def binary_or(a, b):
    """
    Copies a bit if it exists in either operand.
    """
    return a | b


def binary_xor(a, b):
    """
    Copies the bit if it is set in one operand but not both.
    """
    return a ^ b


def binary_once_comp(a):
    """
    It is unary and has the effect of 'flipping' bits.
    """
    return ~a


def binary_left_shift(a, b):
    """
    The left operands value is moved left by the number
    of bits specified by the right operand.
    """
    return a << b


def binary_right_shift(a, b):
    """
    The left operands value is moved right by the number
    of bits specified by the right operand.
    """
    return a >> b
