# def add(name: str, phone_number: int = 5, test='test') -> tuple:
#     return name, phone_number
#
# c = add('4', phone_number=7, test='a')
# print(c)

# def recursion(n):
#     if n>0:
#         result = n + recursion(n-1)
#         print(result)
#     else:
#         result = 0
#     return result
#
# print(recursion(3))

# add = int(input("enter a number: "))
# factorial = 1
# for i in range(1, add+1):
#     factorial = factorial * i
# print(factorial)

# def sum_list(my_list):
#     if len(my_list) == 1:
#         return my_list[0]
#     else:
#         return my_list[0] + sum_list(my_list[1:])
#
# print(sum_list([2, 3, 4, 5, 6])) # [6]
# my_list = [1, 2, 3 ,4]
# print(my_list[1:])

# my_list = [2, 3, 4, 5, 6]
#
# def last_item(list_):
#     return my_list[0]
#
# add1 = last_item(my_list[0])
# add2 = last_item(my_list[1])
# add3 = last_item(my_list[2])
# add4 = last_item(my_list[3])
# add5 = last_item(my_list[4])
# result = add1 + add2 + add3 + add4 + add5
# print(result)

# def add(*args, **kwargs):
#     """this is a add function"""
#     return args, kwargs
#
# print(help(print))

# DRY
# test = lambda a: a + 20
# print(test(7))

# def add(a):
#     return lambda b: b + a
#
# test = add(2)
# print(test(7))

# test = print(5)
# print(type(test))
# print(type(print))
# test(5)
# -----------------------------
# test = 5
#
# def add2(a, b):
#     test3 = 6
#     return a + b
#
# def add(a, b):
#     print(test)
#     test1 = 10
#     x = add2(5, 6)
#     for i in range(1, 5):
#         test4 = i + 1
#     return 'ok'
#
# c = add(2, 3)
# print(c)
# --------------------------------------
# a = 5
# print(type(a))
# b = 'hello'
# print(type(b))

# class Dog:
#     eye = 2
#     ear = 2
#     hands = 2
#     dom = 1
#
#     def __init__(self, color, name, age):
#         self.color = color
#         self.name = name
#         self.age = age
#
#     def eating(self):
#         return f'dog name is {self.name} eating'
#
#
# dog = Dog(name='a', age=5, color='red')
# dog2 = Dog(name='b', age=10, color='blue')
# print(type(dog))
# print(id(dog))
# print(id(dog2))
# print(dog.eating())
# print(dog2.eating())
# --------------------------------------

# class Calculator:
#     """
#     this is calculator class:
#     addad1: int
#     """
#     def __init__(self, addad1, addad2):
#         self.addad1 = addad1
#         self.addad2 = addad2
#
#     def add(self, a=5):
#         return self.addad1 + self.addad2 + a
#
#     def prod(self):
#         return self.addad1 * self.addad2
#
#     def minus(self):
#         return self.addad1 - self.addad2
#
#     def __repr__(self):
#         return f'this is a object from class {self.__class__.__name__} and variable attr {self.addad1} , {self.addad2}'
#
# calculator = Calculator(4 ,6)
#
#
# print(calculator)
# print(calculator.add(5))
# print(calculator.prod())
# print(calculator.minus())

# ------------------------------------
# my_dict = {1: {2: 3}, 2: 20, 3: {2: 3}, 5: 50, 6: 60}
# print(my_dict)
# result = {}
# for key, value in my_dict.items():
#     if value not in result.values():
#         result[key] = value
# print(result)
# -----------------------------------------
# 1
# def find_max_of_two(x, y):
#     if x > y:
#         return x
#     else:
#         return y
#
# def finx_max_of_three(x, y, z):
#     return find_max_of_two(x, find_max_of_two(y, z))
#
# print(finx_max_of_three(3, 4, 5))
# ----------------------------------------
# 2
# def sum_list(*numbers):
#     result = 0
#     for i in numbers:
#         result += int(i)
#     return result
#
# user_input = input('enter numbers: ')
# user_input = user_input.split()
# print(sum_list(2, 3, 4, 5, 6))
# ----------------------------
# a , b , *c = [2, 3, 5, 5, 6, ]
#
# print(a, b ,c)
# ------------------------------
# 4
# def reveres_str(test: str) -> str:
#     return test[::-1]
# print(reveres_str('asdfg123'))
# ----------------------------------
# 7
# def string_letter_count(text: str): # 1asdas3
#     result = {'UpperCount':0, 'LowerCount': 0, 'Other': 0}
#     for item in text:
#         if item.isupper():
#             result['UpperCount'] += 1
#         elif item.islower():
#             result['LowerCount'] += 1
#         else:
#             result['Other'] += 1
#     return result
#
#
# print(string_letter_count('asdfSDASD213ASD23sdcxv$@#a'))
# --------------------------
# 8
# def unique_list(my_list: list) -> list:
#     return list(set(my_list))
# print(unique_list([1,2,3,5,2,1,2,4,5,6,7,8,1]))
# ---------------------------
# 18
# my_code = 'insert table user={}, password={}'
# exec(my_code)
#
# ----------------------------------------
# print('test')




