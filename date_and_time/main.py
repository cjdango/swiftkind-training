import time
import calendar
from datetime import datetime

localtime = time.localtime(time.time())


def get_calendar_now():
    """
    Return calendar for current month as string
    """
    year = localtime.tm_year
    month = localtime.tm_mon
    return calendar.month(year, month)


def get_day_word():
    """
    Return day today as word
    """
    days = list(calendar.day_name)
    return days[localtime.tm_wday]


def get_year_day():
    """
    Return year's day
    """
    return localtime.tm_yday


def get_month_day():
    """
    Return month's day
    """
    return localtime.tm_mday


def get_week_day():
    """
    Return week's day
    """
    return localtime.tm_wday


def get_month():
    """
    Return current month
    """
    return localtime.tm_mon


def get_year():
    """
    Return current year
    """
    return localtime.tm_year


def get_formatted_time():
    """
    Return current formatted time
    """
    return time.asctime(localtime)


def am_pm():
    """
    Return AM or PM for current time
    """
    return datetime.now().strftime("%p")


def get_timezone():
    """
    Return timezone
    """
    return time.strftime('%Z', time.gmtime())


print('get_calendar_now')
print(get_calendar_now())
print('get_day_word', get_day_word())
print('get_year_day', get_year_day())
print('get_month_day', get_month_day())
print('get_week_day', get_week_day())
print('get_month', get_month())
print('get_year', get_year())
print('get_formatted_time', get_formatted_time())
print('am_pm', am_pm())
print('get_timezone', get_timezone())
