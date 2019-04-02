from datetime import datetime


def is_num_good(num):
    """
    Determine if number is good.
    """
    if num != 69 and num != 666:
        return True

    return False


def is_positive(num):
    """
    Determine if number is positive
    """
    if num > 0:
        return True
    else:
        return False


def get_gender(char):
    if char.lower() == 'f':
        return 'Female'
    elif char.lower() == 'm':
        return 'Male'
    else:
        return 'Please choose between f and m'


def is_adult(age):
    """
    Deteremine if age is adult or not.
    """
    if age < 18:
        return False

    return True


def is_teen(age):
    """
    Deteremine if age is teen or not.
    """
    if age > 12 and age < 18:
        return True

    return False


def even_odd(a):
    """
    Determine if number is odd or even.
    """
    if a % 2 == 0:
        return 'even'
    else:
        return 'odd'


def am_pm(hour):
    """
    Determine if hour is am or pm
    """
    if hour < 12:
        return 'AM'
    else:
        return 'PM'


def is_late(hour):
    """
    Determine if hour is late.
    """
    if hour > 9:
        return True
    else:
        return False


def greet_by_time(hour):
    """
    Determine the greeting for the hour
    """
    if hour < 10:
        return 'Good morning'
    elif hour < 20:
        return 'Good day'
    else:
        return 'Good evening'


def eat_what(hour):
    """
    Determine what to eat.
    """
    if hour < 10:
        return 'Breakfast'
    elif hour < 20:
        return 'Lunch'
    else:
        return 'Dinner'


print('is_num_good', is_num_good(68))
print('is_positive', is_positive(-1))

print('is_adult', is_adult(21))
print('is_teen', is_teen(13))
print('even_odd', even_odd(9))

hour = datetime.now().hour
print('am_pm', am_pm(hour))
print('is_late', is_late(hour))
print('greet_by_time', greet_by_time(hour))
print('eat_what', eat_what(hour))

print('get_gender', get_gender('m'))
