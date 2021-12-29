# b = int(input('enter number: '))
# c = int(input('enter number: '))
# a = 5
# d = b + a
# e = b / c
# print(d)
# print(e)
# TypeError, ValueError, ZeroDivisionError

# try:
#     b = int(input('enter number: '))
#     c = int(input('enter number: '))
#     a = 5
#     d = b + a
#     e = b / c
# except ValueError as ex:
#     print('bayad addad vared konid')
#     print(ex)
# except ZeroDivisionError as ex:
#     print('bayad bishtar az 0 vared konid')
#     print(ex)
# else:
#     print(d)
#     print(e)
# finally:
#     print('karam tamoom shod!!!!!!!!')

# try:
#     file_object = open("README.txt")
# except FileNotFoundError as ex:
#     print(ex)
# else:
#     file_object.write("yechizi")
# finally:
#     file_object.close()

# try:
#     with open("README.txt") as file_name:
#         read_data = file_name.read()
#         a = file_name.readlines(20)
# except Exception as ex:
#     print(ex)


# x = -1
# if x < 0:
#     raise Exception("x nabayad az 0 koochik tar bashad")

# class HoomanError(Exception):
#     pass
#
# x = -1
# if x < 0:
#     raise HoomanError("x nabayad az 0 koochik tar bashad")

# -------------------------------------------------
# age = float(1233)
# first_name = "hooman"
# last_name = 'javan'
# number = 5
# welcome = "{fname:^.10} {lname:*>10}, your age is {age:09.2f} welcome home -{number}"
# print(welcome.format(fname=first_name, lname=last_name, age=age, number=number))

# {name:[[fill]align][sign][#][0][width][,][.precision][type]}
#

# print('{:{}{}{}.{}}'.format(2.7182818284, '>', '+', 10, 3))

# welcome = f"{first_name:^.10} {last_name:*>10}, your age is {age:09.2} welcome home -{number}"
# print(welcome)
# --------------------------------


import calculate as cal
from calculate import adder_two_number

result = cal.adder_two_number(5, 7)
print(result)
result = cal.multi_two_number(5, 7)
print(result)
result = cal.minus_two_number(5, 7)
print(result)
result = cal.division_two_number(5, 7)
print(result)
