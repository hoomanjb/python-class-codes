# print(name.capitalize())
# {name:[[fill]align][sign][#][0][width][,][.precision][type]}
# f_name = input("plz inser your first name:")
# l_name = input("plz inser your last name:")
# text = """{first_name} {last_name} welcome"""
# print(text.format(first_name=f_name, last_name=l_name))
# '{1} {0}'.format('one', 'two')
# text = '{:10}'.format('test')
# text = '{:>10}'.format('test')
# text = '{:@<10}'.format('test')
# text = '{:_^10}'.format('test')
# text = '{:_^6}'.format('zip')
# text = '{:.5}'.format('xylophone')
# text = '{:^10.5}'.format('xylophone')
# text = '{:d}'.format(42)
# text = '{:f.10}'.format(3.141592653589793)
# text = '{add:^20.10f}'.format(add=3.1415926535897)
# '{:4d}'.format(42)
# '{:06.2f}'.format(3.1415926535897)
# '{:04d}'.format(42)
# '{:d}'.format(42)
# '{:=5d}'.format((- 23))
# --------------------------------------------
# integer = int(4)
# float_ = float(4)
# complex_ = complex(3)

import math

# print(math.ceil(5.8))
# print(math.floor(5.8))
# print(math.pow(2, 3))
# print(math.sqrt(25))
# print(math.exp(2))
# print("test".lower())
# print(type("test"))
# print(type(math))
# print(2**4)

# a = 4
# b = 5
# c = 6
# print(a < b and b < a)
# print(a < b or b < a)
# print(a < b or b < a)
# print('test'.isalnum())
# a = 'test'
# b = 'test'
# print(a is b)
# print(isinstance(a, float))

# a = 6
# b = 4
# if a == 5 or b == 5:
#     print('a is 5 or b is 4')
# elif b == 4:
#     print('b is 4')
# else:
#     print('a is not 5 or b is not 4')
#
# name = 'anisa'
# print('name is anisa') if name == 'anisa' else print('name is not anisa')
#
# if name == 'anisa':
#     print('name is anisa')
# else:
#     print('name is not anisa')
#
# print("A") if a > b else print("=") if a == b else print("B")

# a = 10
# while a <= 10:
#     if a == 2:
#         print('HAHA')
#         # break
#         a += 3
#         break
#     else:
#         print(a)
#         a += 1
# else:
#     print('loop is over')

# fruits = ["apple", "banana", "cherry"]
# text = 'hooman'
# print(len(text))
# print(len(fruits))
# print(fruits[0])
# print(text[0])
# for item in text:
#     print(item)
#
# print('-------------------------------')
#
# tedad = len(text)
# count = 0
# while count < tedad:
#     print(text[count])
#     count += 1
# fruits = ["apple", "banana", "cherry"]
# text = 'hooman'

# for i in range(1, 11):
#     row = ''
#     for j in range(1, 11):
#         add = '{name:<3d}'.format(name=i * j)
#         row = row + str(add)
#     print(row)
# for i in range(1, 11):
#     print(i)
# else:
#     print('loop is over')
# a = 4
# a = a + 5
# a += 6
#
# z = ''
# z = z + 'salam'
# print(z)
# text = input('plz insert text: ')
# result = " "
# for index in text:
#     result += " " + index
# print(result)

# text = input('enter 3 number: ')
# print(text.split())

# while text != 'stop':
#     text = input('wana continue? or stop?')

text = input('enter 3 number: ')
if isinstance(text, int):
    pass
else:
    text = input('enter 3 number: ')