# name = 'hooman'
# if name == 'ali':
#     result = 'ok'
# else:
#     result = 'nok'
#
# result = 'ok' if name == 'ali' else 'nok'

# #########################
# switch case - match case
# name = ''
# match name:
#     case 'ali':
#         print('ali')
#     case 'taghi':
#         print('taghi')
#     case 'hooman':
#         print('hooman')
#     case _:
#         print('else')
#
# if name == '' and len(name) > 1:
#     print()

# #######################################################
# Loop: while , for

# while -> tedad ro ma nadoonim
# for -> tedad ro bedoonim

# i = 20
# while i <= 10:
#     print(i)
#     i += 1
# else:
#     print('harchiii')

# i = 1
# while i <= 100:
#     if i in [10, 12, 14]:
#         i += 1
#         continue
#     if i % 2 == 0:
#         print(i)
#     else:
#         print('even')
#     if i == 20:
#         break
#     i += 1
# else:
#     print('break')

# continue
# break

# while True:
#     phone_number = input('enter your number: ')
#     if phone_number.isdigit():
#         print('ok')
#         break
#     else:
#         print('incorrect !!!')


# ########################################
# async - go
# for
# name = 'hooman'
# iterable , iterator, generator
# a = [1, 2, 3, 4, 5, 6, 7]
# for item in name:
#     print(item)

# 1 , 2 , 3 , 4
#  multi thret , multi proccess , concorenci
my_list = [1, 2, 3, 10, 'salam', 40]
b = 10
# for item in my_list:
#     print(item)

# index = 0
# for item in my_list:
#     if item == 'salam':
#         print(index)
#     index += 1
#
# for index, item in enumerate(my_list):
#     if item == 'salam':
#         my_list[index] = 'yechizi'
#
# print(my_list)

# a = [[1, 2], [3, 4], [5, 6]]
#
# for item in a:
#     print(item)
#     for inner_item in item:
#         print(inner_item)

# ##################################### #
# list comprehension
# dict comprehension

# my_list = [1, 2, 3, 4, 5, 6, 7, 8]
# new_list = []
#
# for item in my_list:
#     if item % 2 == 0:
#         new_list.append(item)
#
# print(new_list)

# my_list = [1, 2, 3, 4, 5, 6, 7, 8]
# new_list = [item + 2 for item in my_list if item % 2 == 0]
# print(new_list)

# pytonic
# Zen python

# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Flat is better than nested.
# Sparse is better than dense.
# Readability counts.
# Special cases aren’t special enough to break the rules.
# Although practicality beats purity.
# Errors should never pass silently.
# Unless explicitly silenced.
# In the face of ambiguity, refuse the temptation to guess.
# There should be one — and preferably only one — obvious way to do it.
# Although that way may not be obvious at first unless you’re Dutch.
# Now is better than never.
# Although never is often better than right now.
# If the implementation is hard to explain, it’s a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea — let’s do more of those

# import this
# ############################################ #


# def my_func():
#     global a
#     a = 10
#     b = 100000
#     return 'salam'
#
# # local - global
# a = 5
# b = 4
# print(a)
# b = my_func()
# print(a)


# def my_func(fname: str, lname: str = 'khali', *args, **kwargs) -> str:
#     '''
#     in function baraye test sakhte shode
#     :param fname:
#     :param lname:
#     :return:
#     '''
#     print(args)
#     print(kwargs)
#     return fname + ' ' + lname
#
# full_name = my_func('saas', 'vvvv', 4, 5, aa='bb', cc=10)
# print(full_name)

a, *b, c = 3, 5, 6, 5, 6, 8

