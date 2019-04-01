def same(a, b):
    """
    Evaluates to true if the variables on either side of the operator point to the same object and false otherwise.
    """
    return a is b

def not_same(a, b):
    """
    Evaluates to false if the variables on either side of the operator point to the same object and true otherwise.
    """
    return a is not b