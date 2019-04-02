def get_item(key, dct):
    """
    Retrieve item from dct
    """
    return dct[key]


def get_first(dct):
    """
    Return item in first
    """
    return dct[list(dct.keys())[0]]


def get_last(dct):
    """
    Return item in last
    """
    return dct[list(dct.keys())[-1]]


dct1 = {'name': 'cjdango', 'age': 21}

print('get_item', get_item('age', dct1))
print('get_first', get_first(dct1))
print('get_last', get_last(dct1))
