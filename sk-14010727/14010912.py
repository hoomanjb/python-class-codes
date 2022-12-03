# Error Handling
# مدیریت خطا

# a = 10
# b = 0
# print(a/b)

# print(c)

# print('aaa')


# session DB -
# import logging
# a = 10
# b = 0
# try:
#     print(a/b)
# except ZeroDivisionError as ex:
#     logging.error(f'ZeroDivisionError gereftim ba error code: {ex}')
# except TypeError as ex:
#     logging.error(f'TypeError gereftim ba error code: {ex}')
# except NameError as ex:
#     logging.error(f'NameError gereftim ba error code: {ex}')
#
# print('asdasdasdasd')

# a = 10
# b = 0
# try:
#     print(a / b)
# except ZeroDivisionError as ex:  # alias
#     print(ex)
# except Exception as ex:
#     print(ex)
# else:
#     print('else print mishe')
# finally:
#     print('finally print mishe')


# a = 5
# if a < 10:
#     raise Exception('OOOOOW No number below 10')
#
# print('HERE!!!')

# class KavoosiException(Exception):
#     pass

# #####################################################
import datetime

# print(datetime.datetime.now())
# print(datetime.date.today())
# print(datetime.time(hour=10, minute=44, second=12))

# a = datetime.datetime(year=2022, month=12, day=3, hour=19, minute=56, second=45)
# b = datetime.date.today()
# c = datetime.time(hour=10, minute=44, second=12)
# print(a)
# print(type(a))
#
# print(b)
# print(type(b))
#
# print(c)
# print(type(c))

# import jdatetime
# x = jdatetime.datetime.fromgregorian(year=a.year, month=a.month, day=a.day)

# today = datetime.date.today()
# now = datetime.time(hour=10, minute=44, second=12)
# x = datetime.datetime.combine(today, now)
# print(x)

# select national_code from users where brith_date > 2000
# ORM
# a   c   b


# date_string = '10-03-2022 10:24:30'
# format_string = '%m-%d-%Y %H:%M:%S'
#
# x = datetime.datetime.strptime(date_string, format_string)
#
# print(x)

# a = datetime.datetime.now()
#
# b = datetime.timedelta(hours=+15, days=-10, weeks=-14)
#
# print(a + b)

date_string = '10-Dec 10:24:30  $$22'
format_string = '%d-%b %H:%M:%S  $$%y'
print(datetime.datetime.strptime(date_string, format_string))

a = datetime.datetime.now()

print(a.strftime('%B'))
print(a.strftime('%b'))
print(a.strftime('%w'))  # weekday 0-6   0=sunday  6=sat
print(a.strftime('%W'))  # weekNumber
print(a.strftime('%a'))
print(a.strftime('%A'))

print(a.strftime('%y'))
print(a.strftime('%j'))
print(a.strftime('%c'))
print(a.strftime('%C'))
print(a.strftime('%x'))

