# a = 'hello world'
# for i in range(1, 11):
#     print('loop 1')
#     for j in range(1, 11):
#         print('loop2 2')
#         for x in range(1, 11):
#             print('loop3')
#             print(f'{i*j:^4}', end=" ")
#     print()
# flag = 0
# counter = 0
# name = 'anisa'
# # name[0] -> a
# while flag == 0:
#     if name[counter] == 's':
#         flag = 1
#     counter += 1

# my_list = [1, 2, 2,'test', 'test test2', [3, 4, 5, [6, 7, 8]]]
# my_list2 = list((1, 2, 3, 4))
# my_list3 = []
# print(my_list)
# print(my_list2)
# print(my_list[4][3][1])
# my_list[1] = [9, 10]
# print(my_list)
# my_list = [1, 2, 2,'test', 'test test2', [3, 4, 5, [6, 7, 8]]]

# print(7 in my_list[5][3])
# print(my_list[::2])


# my_list = [1, 2, 2,'test', 'test test2', [3, 4, 5, [6, 7, 8]]]
# my_list.append(15)
# my_list[7] = 26 WRONG
# print(my_list)
# print(my_list.count('test'))
# print(my_list[5].count(3))
# print(my_list.index(2))
# new_list = [4, 7, 1, 5, 10, 45, 0]
# new_list2 = ['z', 'a', 'c', 'g']
# new_list2.sort()
# print(new_list2)
# my_list = [1, 2, 2,'test', 'test test2', 'test', [3, 4, 5, [6, 7, 8]]]
# my_list.pop(3)
# print(my_list)
# my_list.remove('test')
# print(my_list)
# my_list = [1, 2, 2,'test', 'test test2', 'test', [3, 4, 5, [6, 7, 8]]]
# new_list = [70, 80]
# my_list.extend(new_list)
# print(my_list)
# my_list.append(new_list)
# print(my_list)
# a = 'hello world'
# print(list(a))

# my_list = [1, 2, 2,'test', 'test test2', 'test', [3, 4, 5, [6, 7, 8]]]
# if 'z' in my_list:
#     print('test exist')
# else:
#     print('wrong')
# for item in my_list:
#     print(item)
# list2 = ['Test1', 'tes2', 'test3']
# new_list = []
# for item in my_list:
#     new_list.append(item)
#
# new_list = [item for item in my_list]
# new_list2 = [item.upper() for item in list2]
# new_list = [4, 7, 1, 5, 10, 45, 0, -3, [6, 7]]
# # new_list.sort(reverse=True)
# print(max(new_list[:-1]))
# print(min(new_list[:-1]))
# new_list = [4, 7, 1, 5, 10, 45, 0, -3, [6, 7]]
# new_list.insert(2, 'test')
# print(new_list)
# ---------------------------------------
# my_tuple = ('test1', 2, 'test1', 4, 'test2')
# my_tuple2 = tuple(('test1', 2, 'test1', 4, 'test2'))
# print(type(my_tuple))
# print(type(my_tuple2))
# print(my_tuple[0])
# my_tuple[1] = 5  WRONG

# print(my_tuple.index(2))
# print(my_tuple.count(2))

# my_tuple = ('test1', 2, 'test1', 4, 'test2')
# if 'test' in my_tuple:
#     print('test exsit')
# else:
#     print('wrong')

# temp_list = list(my_tuple)
# temp_list.append('test5')
# my_tuple = tuple(temp_list)
# print(my_tuple)
# for item in my_tuple:
#     print(item)

# a, b = 1, 2
# print(a)
# print(b)
# my_tuple = ('test1', 2, 'test1', 4, 'test2', 'test3', 5)
# *a, b, c = my_tuple
# print(a)
# print(b)
# print(c)

# ------------------------------------------
# my_set = {1, 3, 4, 6, 7, 1, 5, 7, 8, 12}
# my_set2 = {'a', 'b', 'a', 'v', 'z', 'c'}
# my_set3 = set(('a', 'b', 'a', 'v', 'z', 'c'))
# print(my_set)
# my_set.pop()
# print(my_set)
# print('a' in my_set2)
# my_set.remove(1)
# my_set2.add(89)
# print(my_set2)

# print(my_set.issuperset())

# --------------------------------------------
# my_dict = {'name': 'hooman',
#            'age': 30,
#            'lname': 'javanbakht',
#            'city': ['tehran', 'rasht']}

# print(my_dict['lnamee']) IS NoT Required
# print(my_dict.get('lnamee', 'vojod nadarad'))
# my_dict.pop('city')
# my_dict['name'] = 'anisa'
# print(my_dict)
# print(my_dict.keys())
# print(type(my_dict.values()))
# print(my_dict.items())
#
# for key, value in my_dict.items():
#     print(key, value)

my_dict = {'name': 'hooman',
           'age': 30,
           'lname': 'javanbakht',
           'city': ['tehran', 'rasht']}
# print(my_dict.values())
# if 'hooman' in my_dict.values():
#     print('ok')
# else:
#     print('wrong')
my_dict.update({'phonnumber': 123123123})
print(my_dict)

# int list tuple set str dict bool