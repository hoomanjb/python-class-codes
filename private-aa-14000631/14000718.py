# subject = 'test'

# match subject:
#     case 'test':
#         <action_1>
#     case 'test2':
#         <action_2>
#     case 5:
#         <action_3>
#     case _:
#         <action_wildcard>

# ----------------------------------------
# loop  while  for

# a = 9
# flag = True
# while flag:
#     print(a)
#     a += 1
#     b = 1
#     if a == 15:
#         while b < 10:
#             print(a + b)
#             b += 1
#             if b == 5:
#                 flag = False
#                 break
# else:
#     print('harchi k shod')

# a = 1
# while a <= 20:
#     print(a)
#     print('before check')
#     a += 1
#     if a == 15:
#         a += 1
#         continue
#     print('after check')
# -------------------------------------------------
# name = 'test'
# my_list = [1, 2, 3, 'ali', 4, 5, [9, 10], 20]
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 'asda@gmail.com', 9, 10]

# for index, item in enumerate(my_list):
#     if item == 'ali':
#         print(f'index {index} is equal ali')
#         break
#     print(item)
# my_list[8] = 'test'
# ---------------------------------
# my_list = [1, 2, 5, 7, 'test', [10, 11, [12, 13, [14, 15]]], 'ali', 'ali']
# a = list('test')
# print(my_list)
# print(a)
# print(my_list[5][2][2][1])
# print(my_list[2:7:])
# my_list[5][2][2][1] = 16
# print(my_list)
# if 15 in my_list:
#     print('ok')
# my_list = [1, 2, 5, 7, 'test', [10, 11, [12, 13, [14, 15]]], 'ali', 'ali']
# my_list.append(['akhar', 6, 90])
# my_list.insert(1, ['akhar', 6, 90])
# a = ['akhar', 6, 90]
# for item in a:
#     my_list.append(item)
# my_string = 'test'
# b = my_string.index()
# a = my_list[5][2][2].index(15)
# print(a)
# a = my_list.count('ali')
# print(a)
# my_list = ['z', 'ali', 'test', 'Ali']
# def my_func(a):
#     return a
# my_list.sort(reverse=True)
# my_list.sort(key=my_func)

# print(my_list)

# my_list.extend(['akhar', 6, 90])
# my_list.extend('test)

# print(my_list)
#
# my_list.clear()
# print(my_list)
# my_list = []
# for item in range(21):
#     my_list.append(item)

# my_list = [item for item in range(21)]

# print(my_list)
# --------------------------
def sum_items(my_list: list):
    result = 0
    for item in my_list:
        result += item
    return result

def multiply_items(my_list: list):
    result = 1
    for item in my_list:
        result *= item
    return result

# def find_max_number(my_list: list): # [-1, -7]
#     maximum = my_list[0]
#     for item in my_list:
#         if item > maximum:
#             maximum = item
#     return maximum

# def find_max_number(my_list: list):
#     my_list.sort()
#     return my_list[-1]



# a = [1, -4, 6, -8, 3, 7, -9]
# result = sum_items(my_list=a)
# print(result)
# result = multiply_items(my_list=a)
# print(result)
# print(find_max_number(a))
print('sdsd')


