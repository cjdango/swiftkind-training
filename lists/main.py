def get_first(lst):
    """
    Return item in first index
    """
    return lst[0]


def get_last(lst):
    """
    Return item in last index
    """
    return lst[-1]


def replace(idx, val, lst):
    """
    Replace value in lst[idx] with val
    """
    new_lst = list(lst)
    new_lst[idx] = val
    return new_lst


def remove(idx, lst):
    """
    Remove value in lst[idx]
    """
    new_lst = list(lst)
    del new_lst[idx]
    return new_lst


def show_length(lst):
    """
    Show length of lst
    """
    return len(lst)


def concat(lst1, lst2):
    """
    Concat two list
    """
    return lst1 + lst2


def repeat(lst1, n):
    """
    Repeat lst1 items n times
    """
    return lst1 * n


def is_inside(n, lst):
    """
    Returns True if n is inside lst
    """
    return n in lst


def print_items(lst):
    for x in lst:
        print(x, end=' ')


def count_items(lst, item):
    """
    Returns item count in lst
    """
    return lst.count(item)


lst1 = [1, 2, 3, 4]
lst2 = [4, 3, 2, 1]

print('get_first', get_first(lst1))
print('get_last', get_last(lst1))
print('replace', replace(1, 0, lst1))
print('remove', remove(1, lst1))
print('show_length', show_length(lst1))
print('concat', concat(lst1, lst2))
print('repeat', repeat(lst1, 2))
print('is_inside', is_inside(5, lst1))

print('print_items')
print_items(lst2)

print('\ncount_items', count_items(lst2, 3))
