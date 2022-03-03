from datetime import datetime, time, date, timedelta
import time

# b = datetime.now()

# print(a)
# print(type(a))

# a = date(year=2010, month=5, day=31)
# print(a)
#
# c = time(hour=20, minute=10, second=10)
# print('a')


# today = date.today()
# now = datetime.now()
# print(today)
# print(now)
#
# current_time = time(hour=now.hour, minute=now.minute, second=now.second)
# print(current_time)
#
# print(datetime.combine(today, current_time))


# date_string = "01-25-2021 14:20:30" #01/25/2021 14:20:30
#
# format_string = "%m-%d-%Y %H:%M:%S"
# a = datetime.strptime(date_string, format_string)
# print(type(a))

#
# now = datetime.now()
# print(now)
# a = timedelta(days=-1, hours=-4)
# print(now + a)

# --------------------
# now = datetime.now()
# test = datetime(year=2021, month=10, day=30)
# print(now) # coorent time
# print(now.strftime('%Y')) # current year
# print(now.month)
# print(now.strftime('%B')) # current month name
# print(now.weekday())
# print(now.strftime('%W')) # week number of year
# print(now.strftime('%w')) # weekday of week
# print(now.strftime('%j')) # day of year
# print(now.strftime('%d')) #
# print(now.strftime('%A')) # day name

# import jdatetime
#
# today = jdatetime.datetime.now()
# a = today.togregorian()
# a.year
#
# print(today.fromgregorian(year=2021, month=10, day=31))


def skip_days(days):
    today = datetime.today()
    result = today + timedelta(days)
    return result

# user_days = input('enter days:')
#
# a = skip_days(int(user_days))
# print(a)

def skip_seconds(seconds):
    today = datetime.today()
    print(today)
    result = today + timedelta(seconds=seconds)
    return result

# user_seconds = input('enter seconds:')
#
# a = skip_seconds(int(user_seconds))
# print(a)

# print(time.asctime(time.strptime('2021-50-1', '%Y-%W-%w'))) # avalin roooz hafteye 50om sale 2021


# date_string = 'Jul 1 2021 2:30AM'
#
# result = datetime.strptime(date_string, '%b %d %Y %I:%M%p')
# print(result)

# birthday to now

# a = datetime(year=2021, month=10, day=31, hour=22, minute=23)
# b = datetime(year=1994, month=3, day=5, hour=3, minute=15)
# c = a - b
# hours = c.days * 24
# minuets = hours * 60
# seconds = minuets * 60
# weeks = c.days // 7
# print('days: ' , c.days)
# print('hours: ', hours)
# print('seconds: ', seconds)
# print('weeks: ', weeks)

def is_tuesday(date_string):
    date_object = datetime.strptime(date_string, '%b %d, %Y')
    result = date_object.weekday() == 1 and 14 < date_object.day < 22
    return result


a = 'Oct 19, 2021'
print(is_tuesday(a))