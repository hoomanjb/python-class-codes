# user_input = input("plz enter your number:")
# adad_ragham = user_input.split(sep=' ')
# counter = 0
# for item in adad_ragham[0]:
#     if item == adad_ragham[1]:
#         counter += 1
#     else:
#         continue
# print(f'counter is: {counter}')
#
# print(adad_ragham)
# -------------------------------------------------
# user_input = int(input('enter number: '))
# # x = 5
# if user_input > 1:
#     for item in range(2, user_input):
#         if (user_input % item) == 0:
#             print(f'{user_input} is not a prime number')
#         else:
#             print(f'{user_input} is a prime number')
#             break
# else:
#     print("enter gt 1 ...")
# -----------------------------------
# x = int(input("number:"))
# c = 0
# for i in range(2, x + 1):
#     if x % i == 0:
#         c += 1
#     elif c > 1:
#         break
# if c == 1:
#     print("prime")
# else:
#     print("not prime")

# import random
# x = 1
# y = 99
# pc = random.randint(x, y)
# print(pc)
# me = input("ok?")
# if me == 'd':
#     print('yessss!')
# else:
#     while me != 'd':
#         if me == 'b':
#             x = pc
#             pc = random.randint(x, y)
#             print(pc)
#         elif me == 'k':
#             y = pc
#             pc = random.randint(x, y)
#             print(pc)
#         else:
#             print('please insert k or b or d')
#         me = input('ok?')
#     else:
#         print('tamam')
# a = 5
# my_list = [2, 3, 6, 'salam', True, False, a, [7, 8, 9,[10, 11, 12, [89]]]]
# result = []
# for item in my_list:
#     if item == 89:
#         print(' ok 89')
#     elif isinstance(item, list):
#         for new_item in item:
#             if isinstance(new_item, list):
#                 for new_item2 in new_item:
#                     if isinstance(new_item2, list):
#                         for new_item3 in new_item2:
#                             if new_item3 == 89:
#                                 print('ok 89')
#                             else:
#                                 print('looser')
#     else:
#         print('looser')
# if 89 in my_list:
#     print('ok')
# else:
#     print('wrong')
# my_list = [2, 3, 6, 'salam', True, 6, [], [7, 8, 9,[10, 11, 12, [89]]]]
# print(my_list)
# my_list.append('anisa')
# print(my_list[3:7])
# my_list.insert(4, 'hooman')
# user = '1231231423423'
# print(user.count('3'))
# new_list = ['hooman', 'anisa']
# my_list.extend(new_list)
# my_list.append(new_list)
# my_list.remove('2')
# del my_list[2]
# my_list = [2, 3, 6, 'salam', True, 6, [], [7, 8, 9,[10, 11, 12, [89]]]]
# my_list.pop(2)
# del my_list[-1]
# my_list.clear()
# print(len(my_list))

# user_input = input('enter')
# result = []
# for item in user_input:
#     if item != " ":
#         result.append(int(item))
# print(result)
# result = user_input.split()
# print(result)

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# result = []
# for item in fruits:
#     if item == 'cherry':
#         continue
#     else:
#         result.append(item)
# print(result)
# result = [item for item in fruits if "cherry" not in item]
# print(result)

# result = [x for x in range(10) if x < 5]
# print(result)

# result = [item.upper() for item in fruits]
# print(result)

# result = [x if x != "banana" else "orange" for x in fruits]
# print(result)

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# a = fruits.index("banana")
# fruits[a] = 'orange'
# fruits.reverse()
# print(fruits[::-2])

# my_list = [23, 45, 67, 1, 4, 6, 56]
# result = []
# for item in my_list:
#     if item % 2 == 0:
#         result.append(item)
#     else:
#         continue
# else:
#     print(result)
#     print('finished loop')
# counter = 0
# result = []
# while counter < len(my_list):
#     if my_list[counter] % 2 == 0:
#         result.append(my_list[counter])
#         counter += 1
#     else:
#         counter += 1
#         continue
# else:
#     print(result)
#     print('finished loop')

# my_list = [23, 45, 67, 1, 4, 6, 56]
# result = [item for item in my_list if item % 2 == 0]
# print(result)

# my_list = [23, 45, 67, 1, 4, 6, 56, 6, 7, 1, 45, 9, 10]
# result = []
# for item in my_list:
#     if item in result:
#         continue
#     else:
#         result.append(item)
# print(result)
