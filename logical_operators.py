def both_true(a, b):
    """
    If both the operands are true then return True. False if not.
    """
    return a and b

def any_true(a, b):
    """
    If any of the operands are true then return True. False if not.
    """
    return a or b

def reverse_state(a):
    """
    Used to reverse the logical state of its operand.
    """
    return not a