# a = '12,10,52,23,5'
# my_list = a.split(sep=',')
# print(my_list)
# result = 0
# for item in my_list:
#     result += int(item)
# print(result)

# num = 11
# if num > 1:
#     for i in range(2, num // 2):
#         if (num % i) == 0:
#             print(num, "is not a prime number")
#             break
#     else:
#         print(num, "is a prime number")
# else:
#     print(num, "is not a prime number")

# a = 'hello world'
# b = 'a' + a[1:]
# print(list(b))
#
#

# ----------------------------------------
# tuple ordered,unchange, allow dup
# a = tuple((1,2,3))
# my_tuple = (1, 2, 3, 'sd', [1, 3, 6])
# print(type(my_tuple))
# print(my_tuple[4])
# my_tuple[4][1] = 5
# print(my_tuple)

# if 6 in my_tuple:
#     print('ok')
# b = list(my_tuple)

# a, b = 1, 2

# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
# (a, *b, c, d, e) = fruits
# print(a)
# print(b)
# print(c)
# a = [(1,2), (2,3)]
# ----------------------------------------
# set onordere ,unchange, not allow dup

# my_set = {'test', 1, 2, 'test', 'test2', (1, 3)}
# a = set(('test', 1, 2, 'test', 'test2', [4, 5]))
# print(my_test)
# for item in my_set:
#     print(item)
#
# if 'test' in my_set:
#     print('ok')

# x = ['a', 'A', 's', 'z', 'Z', 'V', 'TEST', 'a', 'b', 'S', 'Z']
# list(set(x)).sort()
# b = set(x)
# x = list(b)
# x.sort()
# print(x)
# result = []
# for item in x:
#     if item not in result:
#         result.append(item)
# result.sort()
# print(result)
# x = ['a', 'A', 's', 'z', 'Z', 'V', 'TEST', 'a', 'b', 'S', 'Z', 'a', 'a', 'a']
# x.remove('a')
# b = set(x)
# b.remove('a')
# x = list(b)
# print(x)
# my_set = {'test', 1, 2, 'test', 'test2', (1, 3)}
# my_set.remove('test')
# a = {'test3'}
# my_set.update(a)
# my_set.add('test4')
# print(my_set)
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# x.intersection_update(y) # eshterak 2ta majmooe
# print(x)
# z = x.intersection(y)
# print(z)
# print(x.symmetric_difference_update(y))
# ------------------------------------
# dict
# my_dict = {"name": ['anisa', 'test'], 'age': 20, 'city': 'tehran'}
# print(my_dict['name'])
# b = my_dict.get('name')
# print(my_dict.keys())
# print(my_dict.values())
# print(my_dict.items())
# my_dict['name'] = 'change'
# print(my_dict)
# if 'name' in my_dict.keys():
#     print('ok')
# my_dict.update({'year': 2021})
# print(my_dict)
# print(my_dict.items())
# # my_dict.pop('age')
# for key, value in my_dict.items():
#     print(key)
#     print(value)

# ------------------------------
# a: required parametere, b: optional parametere
def my_function(a, b=2):
    c = a + b
    return c

a = my_function(a=9, b=5)
v = my_function(a=15, b=1)
c = my_function(a=20, b=3)
z = my_function(a=3, b=7)

print(a + v + c + z)







