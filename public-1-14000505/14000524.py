# my_list = [12, 45, 65, 45, 12, 20, 36]
# EXM 1
# result = sum(my_list)
# result = 0
# for item in my_list:
#     result += item
#     # result = result + item
# print(result)
# -------------------------
# EXM 3
# my_list = [12, 45, 65, 45, 12, 20, 36]
# result = max(my_list)
# maximum = 0
# maximum_index = 0
# for index, item in enumerate(my_list):
#     if item >= maximum:
#         maximum = item
#         maximum_index = index
#     else:
#         continue
# print(f"index is: {maximum_index} and maximum is {maximum}")
# ----------------------------------------
# maximum = 0
# index = 0
# while index <= len(my_list) - 1:
#     if my_list[index] >= maximum:
#         maximum = my_list[index]
#     index += 1
# print(maximum)
# ----------------------------------
# EXM 5
# my_list = ['aba', 'asdd', 'afsdfa', '12341', '45674', 'aa']
# result = 0
# for item in my_list:
#     if len(item) > 2 and item[0] == item[-1]:
#         result += 1
# print(result)
# ----------------------
# EXM 6

# def last(my_list):
#     return my_list[-2]

# my_list = [(1, 3, 4), (9, 1, 4), (4, 6, 2), (2, 2, 5), (4, 4, 4), (1, 5, 7), (3, 6, 1)]
# result = sorted(my_list, key=lambda a: a[-1], reverse=True)
# print(result)
# -------------------------------
# EXM 7
# my_list = [12, 45, 65, 45, 12, 20, 36, 20, 15]
# print(set(my_list))
# result = []
# for item in my_list:
#     if item not in result:
#         result.append(item)
#     else:
#         continue
# result = []
# result = [i for i in my_list if i not in result]
# print(result)
# -----------------------
# 8
# my_list = 0
# # 0 false {} () ''
# if not my_list:
#     print('list is empty')
# -----------------------
# 9
# my_list = [1, 2, 3]
# new_list = list(my_list)
# ------------------------
# 10
# text = "salam hello change street bye anisa python two javanbakht"
# my_list = text.split()
# counter = 7
# result = []
# for item in my_list:
#     if len(item) >= counter:
#         result.append(item)
# print(result)
# --------------------
# 14
# my_list = [7, 8, 110, 120, 25, 44, 48 ,27, 20, 10]
# # result = []
# # for item in my_list:
# #     if item % 2 != 0:
# #         result.append(item)
# result = [item for item in my_list if item % 2 != 0]
# print(result)
# ------------------------
# 16
# result = []
# for item in range(1, 31):
#     result.append(item ** 2)
# result = [item ** 2 for item in range(1, 31)]
# print(result[:5])
# print(result[-5:])
# print(result[5:-5:])
# ---------------
#
# my_list = input('enter some number:')
# result = my_list.split()
# print(result)
# 18
# import itertools
# print(list(itertools.permutations([1,2,3,4])))
# --------------
# 19
# list1 = [1 ,2 ,3 ,4 ,5 ,6 ,7, 2, 1, 76]
# list2 = [2, 1, 3, 3, 5, 9, 12, 4, 0, 1]
# new_list1 = list(set(list1) - set(list2))
# new_list2 = list(set(list2) - set(list1))
# result = new_list1 + new_list2
# print(result)
# list1 = [1 ,2 ,3 ,4 ,5 ,6 ,7, 2, 1, 76]
# list2 = [2, 1, 3, 3, 5, 9, 12, 4, 0, 1]
# found_items = []
# counters = []
# diffs = []
# for item in list1:
#     item_counter = 0
#     for item2 in list2:
#         if item == item2:
#             if item not in found_items:
#                 found_items.append((item))
#             else:
#                 counters.append(item_counter)
#             item_counter += 1
#     diffs.append((item, item_counter))

# -------------------------------
# 21

# my_list = ['hello', 'world', 'bye', 'world']
# print('*'.join(my_list))
# -------------------------
# a = [1, 2, 3]
# b = [4, 5, 6]
# c = a + b
# print(c)
# ---------------------------
# 27
# my_list = [4, 4, 4, 3, 5, 6, 7, 1, 4, 9, 2]
# # result = sorted(my_list)
# # print(result[1])
# result = []
# duplicate_items = set()
# minimum = my_list[0]
# for item in my_list:
#     if item <= minimum:
#         minimum = item
#         result.append(item)







