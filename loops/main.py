def count_10_from(num):
    """
    Count 10 times from the given number
    """

    until = num + 10
    while (num < until):
        print('The count is:', num)
        num += 1


def reverse_count_10_from(num):
    """
    Count 10 times from the given number backwards
    """
    for n in list(range(10)):
        print('The count is:', num - n)


def show_mult_table():
    """
    Show multiplication table
    """
    for i in range(1, 11):
        for j in range(1, 11):
            k = i * j
            print(k, end=' ')
        print()


def bubble_sort(alist):
    """
    Sort list ascending
    """
    for passnum in range(len(alist) - 1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                temp = alist[i]
                alist[i] = alist[i + 1]
                alist[i + 1] = temp
    return alist


def stop_at_8():
    """
    Count to 10 but stop at 8
    """

    for n in range(1, 10):
        if n > 8:
            break
        print(n)


def skip_4():
    """
    Count to 10 but skip 4
    """

    for n in range(1, 10):
        if n == 4:
            continue

        print(n)


def todo_counter():
    """
    Todo counter, showing pass statement
    """

    for n in range(1, 10):
        if n < 8:
            pass
        print(n)


def get_first(list):
    """
    Retrun first item in list using next
    """
    iter_list = iter(list)
    return next(iter_list)


def my_gen():
    """
    Showcase generators
    """
    n = 1
    print('This is printed first')
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n


def extract_even(list):
    """
    Extract even numbers from a list.
    Showcase generator function
    """
    for num in list:
        if num % 2 == 0:
            yield num


print('count_10_from')
count_10_from(20)

print('\nreverse_count_10_from')
reverse_count_10_from(1)

print('\nshow_mult_table')
show_mult_table()

print('\nbubble_sort', bubble_sort([5, 4, 3, 1, 2]))

print('\nstop_at_8')
stop_at_8()

print('\nskip_4')
skip_4()

print('\ntodo_counter')
todo_counter()

print('\nget_first', get_first([56, 2, 3, 4]))

print('\nmy_gen', next(my_gen()))

print('\nextract_even', list(extract_even([1, 2, 3, 4, 5, 6])))
