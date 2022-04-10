# x, y, z = 'h', "z", 1
# my_list = [1, 2, 4, 'hello', [4, 5, [5 ,6]]]
# b = (1, 4, 5)
#
# print(b[0])
# c = list(b)
# c[0] = 7
# # print(a[4][2][1])
#
# name = 'hooman javanbakht'

# print(name.split())
#
# print(name.strip())
#
# print(name.count('h'))

# print(name.find('z'))
# print(name.index('z'))

# print('123123'.isdigit())

# print(my_list.index('h'))

# my_list.pop(1)
#
# my_list.append([7, 8])
#
# print(my_list)
#
# v = {4, 5, 6, 7, 7, 7}
# print(v)
#
# my_list = list(set(my_list))

# #######################################
# a = 200
# b = 300
# if (a < b or a > 100):
#     print('a is lt b')
# elif a == b:
#     print('a == b')
# else:
#     print('a is bt b')
#
# name = 'hooman' if a == 200 else 'ramin'

# ########################################

# while   for
# i = 0
# while i < 10:
#     if i % 2 == 0:
#         i += 1
#         continue
#     if i == 7:
#         break
#     print(i)
#     i += 1
# else:
#     print('there')

# my_list = [1, 2, 4, 'hello', [4, 5, [5, 6]]]
#
# for index, item in enumerate(my_list):
#     if item == 'hello':
#         print(f'find it in index: {index}')
#
# b = []
# for item in range(1, 100):
#     if item % 2 != 0:
#         b.append(item)
#
# a = [item for item in range(1, 100) if item % 2 != 0]
#
# print(a)
# print(b)

# ################################################

# def harchi(a):
#     if a == 0:
#         return 9
#
# my_list = [1, 2, 4, 3, 0]
# my_list.sort(key=harchi)
# print(my_list)

a = "This is a test string from Andrew"
b = a.split()
# print(sorted(b, key=str.lower))

fname = ''
def my_function(fname, lname='javan', *args, **kwargs):
    print(args)
    print(kwargs)
    fname = fname + ' 10 ' + lname
    return fname


a = my_function('hooman', 'harchi', 10, 11, phone=1010)
print(a)
