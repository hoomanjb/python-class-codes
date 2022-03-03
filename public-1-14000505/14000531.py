# 1
# import operator
# my_dict = {1: 2, 3: 4, 5: 6, 7: 8, 9: 10, 11: 3, 12: 6, 13: 0}
# print(my_dict.items())
# sorted_ditc = sorted(my_dict.items(), key=operator.itemgetter(1), reverse=True)
# print(sorted_ditc)
# -------------------------------------------------
# 2
# my_dict = {1: 2, 3: 4}
# my_dict.update({6:8})
# print(my_dict)
# ---------------------------------------
# 3
# dic1 = {1: 10, 2: 20}
# dic2 = {3: 30, 4: 40}
# dic3 = {5: 50, 6: 60}
# new_dict = {}
# for d in (dic1, dic2, dic3): new_dict.update(d)
# print(new_dict)
# ----------------------------------------
# 4
# my_dict = {1: 10, 2: 20, 3: 30, 4: 3, 5: 50, 6: 60}
# if 3 in my_dict.keys():
#     print("key exist")
# else:
#     print("not exist")
# --------------------------------------------
# 5
# my_dict = {1: 10, 2: 20, 3: 30, 4: 3, 5: 50, 6: 60}
#
# for key, value in my_dict.items():
    # print(f"{key} ----> {value}")
# ---------------------------------------
# 6
# my_dict = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
# last = input("enter a number: ")
# # my_dict = {}
# # for item in range(1, int(last) + 1):
# #     my_dict[item] = item ** 2
# my_dict = {item: item ** 2 for item in range(1, int(last) + 1)}
# print(my_dict)
# --------------------------------------------
# 8
# dic1 = {1: 10, 2: 20}
# dic2 = {3: 30, 4: 40}
# new_dict = dic1.copy()
# new_dict.update(dic2)
# print(new_dict)
# print(dic1)
# ----------------------------------------------
# 10
# my_dict = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
# print(sum(my_dict.values()))
# ----------------------------------------------
# 11
# my_dict = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
# result = 1
# for value in my_dict.values():
#     result *= value
# print(result)
# ------------------------------------------
# 12
# my_dict = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
# if 6 in my_dict:
#     del my_dict[3]
# my_dict.pop(4)
# print(my_dict)
# ---------------------------------------
# 13
# keys = ['name', 'age', 'number']
# values = ['anisa', 30, '1234']
# my_dict = dict(zip(keys, values))
# print(my_dict)
# ----------------------------
# 15
# my_dict = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
# print(my_dict)
# maximum = max(my_dict.values())
# print(maximum)
# -----------------------------
# 17
# my_dict = {1: {2: 3}, 2: 20, 3: {2: 3}, 5: 50, 6: 60}
# print(my_dict)
# result = {}
# for key, value in my_dict.items():
#     if value in result.values():
#         result[key] = value
# print(result)
# -----------------------------------------
# 18
# 0 False [] {} () '' ""
# d = {}
# if not d:
#     print(" d is empty")
# ------------------------------------
# 19
# from collections import Counter
# dic1 = {1: 10, 2: 20}
# dic2 = {1: 30, 4: 40}
# dic3 = Counter(dic1) + Counter(dic2)
# print(dic3)
# ----------------------------------------
# 20
# my_dict = {1: 3, 2: 20, 3: 4, 5: 50, 6: 60, 7: 0}
# uniqe_value = set(my_dict.values())
# print(uniqe_value)
# ------------------------------------------
# 21 ******************
# my_dict = {'1': ['a', 'b'], '2': ['c', 'd']}
# values = my_dict.values()
# print(values)

# for item in values:
#     for in_item in item:
#         print(in_item)

# import itertools
# my_iter = [my_dict[k] for k in sorted(my_dict.keys())]
# for item in itertools.product(*my_iter):
#     print(''.join(item))
# ----------------------------------------------
# 27
# my_list = [1, 2, 3, 4]
# result = temp_dict = {}
# a = id(result)
# b = id(temp_dict)
# for item in my_list:
#     c = id(temp_dict)
#     temp_dict[item] = {}
#     temp_dict = temp_dict[item]
#     d = id(temp_dict)
# print(result)
#{1: {2: {3: {4: {}}}}}
# ------------------------------------------

# def my_function():
#     a = 'hello world'
#     b = a.split()
#     return b

# def my_function(a, b):
#     return a + b

# c = my_function()
# print(c)

# def my_function(adad_aval: int, adad_dovom: int = 5, *args, **kwargs) -> int:
#     print(args)
#     print(kwargs)
#     return adad_aval + adad_dovom

# d = my_function(2, 3)
# c = my_function(3.5 , 5)
# d = my_function(3 , 5, 3, 5, 6, name='anisa', age=40)
# print(d)


def getting_unique_value(my_dict: dict) -> set:
    return set(my_dict.values())

d = {1: 3, 2: 20, 3: 4, 5: 50, 6: 60, 7: 0}
print(getting_unique_value(d))

