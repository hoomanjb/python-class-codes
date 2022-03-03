# f = open('new_file', mode='r')
# print(f.read(5))
# print(f.readline())
# print(f.readline())
# print(f.readline())
# for line in f:
#     print(line)
# f.close()

# try:
#     f = open('new_file', mode='r')
# except Exception as ex:
#     print(ex)
# finally:
#     f.close()

# file = open('new_file2', mode='w')
# file.write('this is a append call')
# file.close()

# with open('new_file', mode='r') as file:
#     print(file.readlines())

# flag = True
# while flag:
#     with open('new_file', mode='r') as file:
#         print(file.readline())
# ------------------------------------
import datetime

# print(datetime.datetime.now())
# a = datetime.date(year=2020, month=5, day=12)
# print(type(a))
# print(a.day)
# print(a.replace(year=2021))
# print(a.strftime('%Y:%m:%d--%a-%b-%p'))
# print(a.strftime('%a'))
# print(a.strftime('%A'))
# print(a.strftime('%w'))
# print(a.strftime('%b'))
# print(a.strftime('%y'))
# print(a.strftime('%H'))
# print(a.strftime('%I'))
# print(a.strftime('%p'))
# print(a.strftime('%W'))
# print(a.strftime('%x'))

# my_time = datetime.time(hour=23, minute=23, second=23)
# print(type(my_time))
#
# my_datetime = datetime.datetime(year=2020, month=4, day=10, hour=20, minute=4, second=23)
# print(my_datetime)

# today = datetime.datetime.today()
# print(today)

# date = "2020-01-31 14:20:35"
# date2 = "2021-06-12 14:20:35"
# format_string = "%Y-%m-%d %H:%M:%S"
# b = datetime.datetime.strptime(date, format_string)
# print(type(b))
# from datetime import datetime, timedelta
# now = datetime.now()
# tomorow = timedelta(days=-5, hours=-4, minutes=+20)
# print(type(tomorow))
# print(now + tomorow)
# -----------------------------------------------------

# import datetime, time
# today = datetime.datetime.now()
# print(f'this is a current datetime {today.now()}')
# print(today.year)
# print(today.strftime('%b'))
# print(today.strftime('%W'))
# print(today.strftime('%A'))
# print(today.strftime('%j'))

# import datetime
#
# class MyDateTimeClass:
#     now = datetime.datetime.now()
#     today = datetime.datetime.today()
#     my_format_string = "%Y-%m-%d %H:%M:%S"
#
#     @staticmethod
#     def convert_str_to_datetime(text, format_string):
#         return datetime.datetime.strptime(text, format_string)
#
#     def my_current_time(self):
#         return self.now.hour
#
#     def show_other_days(self, day):
#         temp = datetime.timedelta(days=day)
#         return self.now + temp
#
#     def show_from_timestamp(self, timestamp: int):
#         return datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
#
#     def convert_date_to_datetime(self):
#         return datetime.datetime.combine(self.now, datetime.datetime.min.time())
#
#     def show_other_seconds(self, second):
#         temp = datetime.timedelta(seconds=second)
#         return self.now + temp
#
#     def convert_date_to_days(self):
#         # return (self.today - datetime.datetime(self.today.year, 1, 1)).days + 1
#         return self.today.strftime('%j')
#
#     # 15 datetime
#     def get_all_sundays_date(self, year):
#         first_day = datetime.date(year, 1, 1)
#         result = []
#         first_day += datetime.timedelta(days=6 - first_day.weekday())
#         print(first_day)
#
#
#
# my_datetime = MyDateTimeClass()
# print(my_datetime.convert_str_to_datetime('Jul 1 2014 2:43PM', '%b %d %Y %I:%M%p'))
# print(my_datetime.my_current_time())
# print(my_datetime.show_other_days(10))
# print(my_datetime.show_from_timestamp(12345215))
# print(my_datetime.convert_date_to_datetime())
# print(my_datetime.show_other_seconds(-10))
# print(my_datetime.convert_date_to_days())
# print(my_datetime.get_all_sundays_date(2021))
# yield


# -----------------------------------------------
# import json
# x = '{"name": "anisa", "age": 20, "city": "tehran"}'
# a = json.loads(x)
# print(a['name'])
# print(type(a))
# b = json.dumps(a)
# print(json.dumps("test"))




