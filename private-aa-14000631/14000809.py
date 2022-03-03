# a = ("a", 2, "test", [1, 2], 2)
# b = tuple((1, 2, 3))
# print(type(a))
# print(type(b))
# print(a[2])
# c = list(a)
# c[2] = 5
# a = tuple(c) B= tuple(c)
# print(a)

# print(a[-1])

# if "a" in a:
#     print('is exist')

# a = ("a", 2, "test", [1, 2], 2)
# b = list(a)
#
# print(a.count(2))
# print(a.index("test"))

# my_tuple = (1, 2, 3, 4, 5, 6, 7)
# *a, b, c = my_tuple
# print(a, b, c)

# my_tuple = (1, 2, 3, 4, 5, 6, 7)
# for item in my_tuple:
#     print(item)

# a = (1, 2, 3)
# b = (4, 5)

# c = a + b # sum
# print(c * 2) # multi values

# -------------------------------------------
# SET
# my_set = {"test1", "test2", "test3", 2, 2, (1, 3), 2, 2}

# print(my_set)
#
# a = [1, 2, 2, 2]
# b = set(a)
# print(b)

# a = list(my_set)
# print(a)
# my_set = {"test1", "test2", "test3", 2, 2, (1, 3), 2, 2}
# my_set2 = {8, 9}
# my_list = [10, 11]
# my_set.add(5)
# print(my_set)

# my_set.update(my_set2)
# my_set.update(my_list)
# my_set.remove("test5")
# my_set.discard('test5')
# a = {1, 2, 3}
# a.pop()
# print(a)
# my_set.clear()
# del my_set

# for item in my_set:
#     print(item)

# x = {'a', 'b', 'c'}
# y = {'d', 'e', 'f'}

# z = x.difference(y)
# z = x.difference(y)
# x.difference_update(y)
# print(z)
# print(x)
# z = x.intersection(y)
# x.intersection_update(y)
# print(z)
# print(x)
# z = x.isdisjoint(y) # Return True if two sets have a null intersection.
# print(z)
#
# if "a" in x:
#     print('is exist')

# x = {'a', 'b'}
# y = {'a', 'b', 'c'}

# z = x.issubset(y)
# z = x.issuperset(y)
# print(z)

# z = x.union(y)
# v = x + y
# print(z)
# print(v)
# ---------------------------------
# Dictionary
# my_dict = {'name': 'hooman', 'last_name': 'javan',
#            'phone_number': 132456,
#             'class_nubers': [1, 2, 3]}

# print(my_dict['name2'])
# print(my_dict.get('name', 10))

# print(my_dict.keys())
# print(my_dict.values())
# print(my_dict.items())
# print(my_dict)
# my_dict['name'] = 'ali'
# print(my_dict)

# my_dict = {'name': 'hooman',
#            'last_name': 'javan',
#            'phone_number': 132456,
#            'class_numbers': [1, 2, 3]
#            }

# print(my_dict.items())
#
# if 'hooman' in my_dict.values():
#     print('is exist')
#
# a = [1, 2, 3, [4, 5], ('name', 'hooman')]
#
# if 'hooman' in a[4]:
#     print('is exist')

# my_dict.update({'year': 2021})
# my_dict['color'] = 'red'
# print(my_dict)

# my_dict.pop('color')
# print(my_dict)
# my_dict.popitem()
# print(my_dict)
# my_dict.popitem()
# print(my_dict)
# my_dict.clear()

# my_dict = {'name': 'hooman',
#            'last_name': 'javan',
#            'phone_number': 132456,
#            'class_numbers': [1, 2, 3]
#            }
#
# for key, value in my_dict.items():
#     print(key)
#     print(value)

my_dict = {'name': 'hooman',
           'last_name': 'javan',
            'phone_number': 132456,
            'class_numbers': [1, 2, 3]
            }
def items(key1,item):
    if key1 in item:
        print("is exist")
    else:
        print("is not exist")
key1= 'arash'
items(key1,my_dict)
#end


