def get_first(tpl):
    """
    Return item in first index
    """
    return tpl[0]


def get_last(tpl):
    """
    Return item in last index
    """
    return tpl[-1]


def replace(idx, val, tpl):
    """
    Replace value in tpl[idx] with val
    """
    new_lst = list(tpl)
    new_lst[idx] = val
    return tuple(new_lst)


def remove(idx, tpl):
    """
    Remove value in tpl[idx]
    """
    new_lst = list(tpl)
    del new_lst[idx]
    return tuple(new_lst)


def show_length(tpl):
    """
    Show length of tpl
    """
    return len(tpl)


def list_to_tuple(lst):
    """
    Converts list to tuple to make it immutable
    """
    return tuple(lst)


def tuple_to_list(tpl):
    """
    Converts tuple to list
    """
    return list(tpl)


def get_highest(tpl):
    """
    Returns highest item in tpl
    """
    return max(tpl)


def get_lowest(tpl):
    """
    Returns lowest item in tpl
    """
    return min(tpl)


def is_inside(n, tpl):
    """
    Returns True if n is inside tpl
    """
    return n in tpl


lst1 = ['a', 'b', 'c']
tpl1 = (1, 2, 3, 4)
tpl2 = (4, 3, 2, 2, 1)

print('get_first', get_first(tpl1))
print('get_last', get_last(tpl2))
print('replace', replace(1, 0, tpl1))
print('remove', remove(1, tpl2))
print('show_length', show_length(tpl2))
print('list_to_tuple', list_to_tuple(lst1))
print('tuple_to_list', tuple_to_list(tpl1))
print('get_highest', get_highest(tpl2))
print('get_lowest', get_lowest(tpl1))
print('is_inside', is_inside(3, tpl2))
