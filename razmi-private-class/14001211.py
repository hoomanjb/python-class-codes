# name = 'hooman'

# print(name.find('z'))
# print(name.index('z'))

# print('a' in name)
#
# print(name.upper())
# print(name.lower())

# print(name.capitalize())
# print(name.count('a', 2, 4))
# print(name.endswith('z'))
# a = '1231223123'
# print(a.isdigit())
# a = [2, 'salam', '1231']

# itarable -> [] '' () {}

# print(name.join(['@', ',']))

# for item in name:
#     print(item)

# print(name)
# print(name.replace('o', 'z', 1))
# print(name)
# name = 'hooman@javan.com'
# name = 'salam chetori che khabar'
# print(name.split())
# name = '       a     '
# print(name.strip())
#
# a = 'hello'
# b = 'world'
# print(a + b)
#
# print('*' * 20)

# ############################################
# text = 'welcome  {0}, to {1} web!'
# result = text.format('hooman', 'python class')
# from config import fill, block_size
# text = 'welcome {name:{fill}^.10}, to {web_name} web! count: {addad:07.4f}'
# result = text.format(
#     name='hoomannnnnnnnnnnnnn',
#     web_name='python class',
#     addad=142.1231231231,
#     fill=fill)
# print(result)

# a = 123.9
# print(int(a))
# b = 5
# print(float(b))

# for i in range(1, 11):
#     a = '{} '
#     for j in range(1, 11):
#         a += a.format(i*j)
#     print(a)

# name = 'hooman'
# web_name = 'python'
# addad = 3.5
# text = f'welcome {name:*^.10}, to {web_name} web! count: {addad:07.4f}'

# user_input = input('enter your name and your age: ')
# print(user_input.split())
# ################################
# 00000011 & 00000001 >>
# import math
# a = 3.5
#
# print(math.ceil(a))
# print(math.floor(a))
# print(math.factorial(3))

# a = 5
# a += 10 # a = a + 10
# ###########################33
# True 1 ' ' [1] (2) {'a': 2}
# False 0 '' [] () {}

# print(isinstance(4, str))
# print(1 == 4)
# print(1 != 4)
# print(2 >= 5)
# print('a' not in 'hooman')
# ###########################################33
# IF
# a = 4
# b = 3
# if (a > b) and (a > 4):
#     print('a is qt b')
# elif a == b:
#     print('a is equal b')
# else:
#     print('a is not gt b')

# if True:
#     print('hello')

# a = 5
# print('helloooo') if a == 5 else print('byyyyyy')
# result = 'helooo' if a == 4 else 'world'

# ################################
# x = 'a'
# match x:
#     case 'a':
#         print('a')
#     case '_':
#         print('_')
# ####################################
# for
# while
# i = 1
# while i < 6:
#     print(i)
#     i += 1
#
# for i in range(6):
#     print(i)

# i = 0
# while True:
#     print('hello')
#     if i == 15:
#         print('i is 15')
#         break
#     else:
#         print(f'i is {i}')
#     i += 1

i = 0
while True:
    print('hello')
    if i % 2 == 0:
        print(f'i is {i} -> first one')
        i += 1
        continue
    else:
        print(f'i is {i} -> second one')
    if i == 100:
        break
    i += 1




