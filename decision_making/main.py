from datetime import datetime

def is_adult(age):
    """
    Deteremine if age is adult or not.
    """
    if age < 18:
        return False

    return True


def even_odd(a):
    """
    Determine if number is odd or even.
    """
    if a % 2 == 0:
        return 'even'
    else:
        return 'odd'


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


print('is_adult', is_adult(21))
print('even_odd', even_odd(9))

hour = datetime.now().hour
print('greet_by_time', greet_by_time(hour))