# factorial

# 5! = 5 * 4!
# 4! = 4 * 3!

# 1! = 1 * 1

# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
#
# result = factorial(5)
# print(len(str(result)))

# def my_func(item1: str, item2: int = 0, *args, **kwargs) -> list[int]:
#     return [1, 2, 3]


# x = lambda a, b: a + 10 + b
# print(x(5, 6))

# def my_func(n, a):
#     return a * n, 'test', 'test12'
#
# test, test2, test3 = my_func(5, 7)
# test(6)
# print(test(7))

# ###############################################
# The LEGB Rule
# Local
# Enclosing
# Global
# Built-in

# ###############################################
# String - str -> sequence
# List -> ordered, changeable , allow duplicate value
# my_list = ['apple', 'orange', 'cherry', 'banana', [4, 6, 7]]
#
# print(my_list[0])
# print(my_list[-1])
# print(my_list[:3])
#
# if 'apple' in my_list:
#     print('ok')
#
# if 7 in my_list:
#     print('ok')
#
# if 'c' in my_list:
#     print('ok')
#
# print(isinstance(my_list, list))
#
# for index, item in enumerate(my_list):
#     if isinstance(item, list):
#         print(item, index)
#         my_list.pop(4)
#
# print(my_list)

# my_list = ['apple', 'orange', 'cherry', 'banana', [4, 6, 7]]
# del my_list
# my_list.pop(9
# print(my_list.index('asdsasd'))

# for item in my_list:
#     if item == 'asdasd':
#         print('ok')

# my_list.append([6, 8, 9])
# print(my_list)
#
# my_list.insert(2, 'ok')
# print(my_list)

# my_list.sort()
# my_list.reverse()

# my_list = ['apple', 'orange', 'cherry', 'banana', 'AAA', 'T', 'L']
# my_list.sort(key=str.lower)
# print(my_list)

# Code Asci
# my_list.append([6, 7, 8])
# print(my_list)
# my_list.extend([10, 11, 12])
# print(my_list)

# my_list = ['a', 's', 'f', 'q', 'A']
# print(max(my_list))
# print(min(my_list))


# my_list = [2, 4, 6, 7, 5, 2, 8]
# my_list[2] = 999
# print(my_list)
# result = []
# for item in my_list:
#     result.append(item*2)
# print(result)
#
# result = [item*2 for item in my_list]
# print(result)

# #############################################
# Tuple ordered, unchangeable, allow duplicate
# my_tuple = (1, 5, 7, 1, 'hello', [4, 6], (99, 100))
# my_tuple = tuple((1, 5, 7, 1, 'hello', [4, 6], (99, 100)))

# print(my_tuple[4])
#
# if 'hello' in my_tuple:
#     print('ok')
# my_tuple[2] = 'yechizi'
# a = list(my_tuple)
# a[2] = 99
# my_tuple = tuple(a)
# print(my_tuple)

# my_tuple = tuple((1, 5, 7, 1, 'hello', [4, 6], (99, 100)))
# print(my_tuple.index(44))
# print(my_tuple.count(99))

# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

# a, b, *c = fruits
# print(a)
# print(b)
# print(c)

# d = fruits * 2
# print(d)

# ##########################################
# Write a Python program to sum all the items in a list.

# def my_sum(my_list: list[int]) -> int | str:
#     result = 0
#     if isinstance(my_list, list):
#         for item in my_list:
#             if isinstance(item, int):
#                 result += item
#         return result
#     else:
#         return 'آقا مگه نگفتم لیست بهم بده'
#
# print(my_sum(['chert', 1, 4, 5]))
# print(sum(['chert', 1, 4, 5]))
# ##################################################
# Set  unordered, unchangeable, not allow duplicate

my_set = ['test1', 'test2', 'test3', 'salam', 2, 66, 10, 'test2', 'salam']
print(my_set)
a = set(my_set)
my_list = list(a)
print(my_list)