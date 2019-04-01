def add(a, b):
    """Adds a and b."""
    return a + b

def sub(a, b):
    """Subtract b from a."""
    return a - b

def mult(a, b):
    """Multiply a by b"""
    return a * b

def div(a, b):
    """Divide a by b"""
    return a / b

def get_remainder(a, b):
    """
    Divides left hand operand by right hand operand and returns remainder
    """
    return a % b

def pow(a, b):
    """
    Performs exponential (power) calculation on operators
    """
    return a ** b

def floor_div(a, b):
    """
    The division of operands where the result is the quotient in which the digits 
    after the decimal point are removed. But if one of the operands is negative, 
    the result is floored, i.e., rounded away from zero (towards negative infinity) 
    """
    return a // b