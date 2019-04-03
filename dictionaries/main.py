import json


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


def remove(key, dct):
    """
    Removes an item from dct
    """
    new_dict = dict(dct)
    del new_dict[key]
    return new_dict


def merge(dct1, dct2):
    """
    Merge two dictionaries
    """
    return dict(dct1, **dct2)


def show_length(dct):
    """
    Show length of dct
    """
    return len(dct)


def get_or_none(key, dct):
    """
    Get dct[key] or return None
    """
    return dct.get(key, None)


def dict_to_json(dct):
    """
    Converts dict to json
    """
    return json.dumps(dct)


def is_dict(arg):
    """
    Confirms arg is dict
    """
    return isinstance(arg, dict)


def is_in(value, dct):
    """
    Determine if value is in dct
    """
    return value in list(dct.values())


dct1 = {'name': 'cjdango', 'age': 21}
dct2 = {'birthday': 23, 'address': 'trese'}

print('get_item', get_item('age', dct1))
print('get_first', get_first(dct1))
print('get_last', get_last(dct1))
print('remove', remove('name', dct1))
print('merge', merge(dct1, dct2))
print('show_length', show_length(dct1))
print('get_or_none', get_or_none('nam', dct1))
print('dict_to_json', dict_to_json(dct1))
print('is_dict', is_dict(dct2))
print('is_in', is_in('trese', dct2))
