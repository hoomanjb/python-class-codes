# import calculator.sum_number as calsum
# from calculator.sum_number import add_2_number
#
# print(add_2_number(5, 9))
# import datetime
# from datetime import timedelta
# ##########################################

from datetime import date, time, timedelta
import datetime as dt
# import datetime

# a = dt.datetime.now()
# b = date(year=1999, month=7, day=25)
# print(type(a))
# print(type(b))

# today = date.today()
# today2 = dt.datetime.today()
# print(today)
# print(today2)
# current_time = time(hour=12, minute=23, second=10)

# d = dt.datetime.combine(today, current_time)
# print(d)
# date_str = "01-24-2021 12:25:36"
# format_str = "%m-%d-%Y %H:%M:%S"
#
# f = dt.datetime.strptime(date_str, format_str)
# print(type(f))
# timedelta_object = timedelta(days=-5, hours=-12, minutes=5)
# print(timedelta_object)
# t = f + timedelta_object
# print(f)
# print(t)
# ########################################
# import jdatetime as jdt
# import datetime as dt
# from jdatetime import datetime

# print(jdt.datetime.now())
# a = dt.datetime.now()
# b = jdt.date.fromgregorian(day=10, month=5, year=2020)
# c = jdt.date.togregorian(a)
# print(c)

# ################################3
import re

s = 'foo143bar'
# if re.search('^a', s):
# if re.search('[0-9][0-4][0-9]', s):
# if re.search('[a-z][0-4][0-9]', 'a19'):
# if re.search('[a-zA-Z][0-4][0-9]', 'A19'):
# if re.search('[0-9]*[0-9]', 'foo13bar'):
# if re.search('[0-9].[0-9]', 'foo145bar'):
# if re.search('[0-9].+', 'foo1a'):

# a = open('test.txt', "r")

# with open('test.txt', "r") as ft:
#     for line in ft.readlines():
#         if re.search('chetori[7-9]', line):
#             print('peydash kardam')
#
# if re.search('[0-9].+', 'foo1'):
#     print('find it')
# else:
#     print('not found')

# if re.search('^123$', '124'):
# if re.search('^[^0-9]', '123'):
# if re.search('[^0-9]$', '123asd'):
# if re.search('[^0-9]\.', '123asd'):
# if re.search('\w', 'asd123'):
# if re.search('^\d$', '12asd3'):
# if re.search('^$', ''):

if re.search('^ $', ' '):
    print('find it')
else:
    print('not found')

