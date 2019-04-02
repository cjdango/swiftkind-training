def get_first_char(string):
    """
    Get first character of string
    """
    return string[0]


def get_last_char(string):
    """
    Get last character of string
    """
    return string[-1]


def say_str(a, n):
    """
    Say a n times
    """
    return a * n


def truncate(string, b, c):
    """
    Truncate string to b chars and append c
    """
    return string[:b] + c


def split_by_space(string):
    """
    Explode string
    """
    return string.split()


def split_by_min(string):
    """
    Explode string by min
    """
    return string.split(min(string))


def split_by_max(string):
    """
    Explode string by max
    """
    return string.split(max(string))


def join_push_0(lst):
    """
    Implode list then append 0
    """
    return '-'.join(lst) + '-0'


def join_remove_last(lst):
    """
    Implode list then remove last char
    """
    return '-'.join(lst)[:-1]


def join_remove_last_two(lst):
    """
    Implode list then remove last two char
    """
    return '-'.join(lst)[:-2]


print('get_first_char', get_first_char('cjdango'))
print('get_last_char', get_last_char('cjdango'))
print('say_str', say_str('hello', 2))
print('truncate', truncate('hellohello hello hellohello', 8, '...'))
print('split_by_space', split_by_space('hello world'))
print('split_by_min', split_by_min('aaaaa.aaaa.aaaa.a'))
print('split_by_max', split_by_max('asdazasdccazadazzzasdadz'))
print('join_push_0', join_push_0(['1', '2', '3', '4']))
print('join_remove_last', join_remove_last(['1', '2', '3', '4']))
print('join_remove_last_two', join_remove_last_two(['1', '2', '3', '4']))
