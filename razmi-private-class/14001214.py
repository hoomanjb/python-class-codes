# counter = 0
# a = 50
# while counter < 20:
#     if counter == 10:
#         print('break')
#     print('loop again')
#     counter += 1
# else:
#     print('elseeeeeee')

# ##########################
# LIST
# a = [3, 5, 'hello', [9, 8, ['a']], 'world']

# print(a[2])
# print(a[3])
# print(a[3][2][0])

# if 9 in a:
#     print('exist')
# print(a[1:3])

# a = [3, 5, 'hello', [9, 8, ['a']], 'world']
# print(a.index('world'))
# print(a.find('z'))
# for item in a:
#     if item == 5:
#         print('5 exist')
# a[3] = 8
# print(a)
# b = a.append('yechizi')
# print(b)
# b = a.index('world')
# print(b)
# a.append(['yechizi', 5, 7])
# # print(a)
# a.extend(['aaaaa', 6, 7, 1])
# print(a)
# print(len(a))
# for item in a:
#     print(item)

# comprehension
# b = []
# for item in a:
#     if item != 'yechizi':
#         b.append(item)
#
# b = [item for item in a if item != 'yechizi']

# print(b)
# b.remove('hello')
# print(b)
# b.pop(1)
# print(b)
# b.clear()
# print(b)

# print(b)
# b.insert(1, 'index')
# print(b)
# a = [3, 5, 'hello', [9, 8, ['a']], 'world']
# # b= [5, 6, 7, 8,1,3,7]
# b = ['a', 'A', 'y', 'Z', 'u', 'z']
#
# print(b)
# b.sort(key=str.upper)
# print(b)

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
#
# a = [item for item in fruits if 'k' in item]
# b = [item.upper() for item in fruits if len(item) > 5]
#
# print(b)

# ######################################
# TUPLE
a = (('4', '5', '7'))
b = (1, 2, 3, 4)
# print(type(b))
# b[1] = 8
# print(b)
#
# print(b[1:3])
#
# if 4 in b:
#     print('exist')
# c = list(b)
# print(c)
# b = tuple(c)

# print(b.index(3))
# print(b.count(1))

# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
#
# (a, *b, c) = fruits
#
# print(a)
# print(b)
# print(c)
#
# print(fruits * 3)

# #############################
# SET
# [(user, password), (age, gender), ()]
# my_set = {'a', 'a', 'b', 'c', 'z', 'a'}
# print(my_set)
#
# for item in my_set:
#     print(item)

# my_set.add('g')
# print(my_set)

# new_set = {'j', 'i', 'v'}
# my_set.update(new_set)
# my_set.remove('x')
# my_set.discard('x')
# my_set.pop()
# my_set = {'a', 'a', 'b', 'c', 'z', 'a', 'v'}
# new_set = {'j', 'i', 'v'}
# x = my_set.union(new_set)
# my_set.intersection_update(new_set)
# v = my_set.intersection(new_set)
# v = my_set.symmetric_difference(new_set)
# my_set.symmetric_difference_update(new_set)
# print(v)
# print(my_set)
# print(new_set)
# print(x)

# #################
# a = ['a', 'a', 'b', 'c', 'z', 'a', 'v']
a = list(set(['a', 'a', 'b', 'c', 'z', 'a', 'v']))
print(a)
