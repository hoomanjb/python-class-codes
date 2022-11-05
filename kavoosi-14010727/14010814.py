# Format string

# text = """{}-{} ({{}})""".format('one', 'two')
# a = 'one'
# b = 'two'
# text = f'{a}-{b} ({{}})'

# Syntax Format string  {name:[[fill]align][sign][width][.precision][type]}
# align: < > ^

# align = <
# width = 20
# lan = eng ,

# text = '{fname} - {lname}'.format(fname='hooman', lname='javanbakht')
# text = '{fname:#^.10} - {lname:15}'.format(fname='hooman', lname='javanbakht')

# text = '{fname:#^10.8} - {lname:15}'.format(fname='hoomannn', lname='javanbakht')

# text = '{:0.10f}'.format(45.145641231234)
# text = '{:{}{}{}.{}}'.format(3.456564, '>', '+', 10, 3)
# align, sign, width, pres = '>', '+', 10, 3
# text = f'{3.456564:{align}{sign}{width}.{pres}}'
# text = f'{100003453450:,}'
# a = 45.145641231234
# text = f'{a:0.10f}'
# print(text)

# ##########################################
# Number
# a = 16_546_132_165_465
# a = 10
# b = float(a)
# print(type(a))
# print(type(b))
# c = int(b)
# print(type(c))
# print(b)
# d = 10 +3j
# print(type(d))


# ######################################
# boolean
# True  : 1 22 3 'a' ' ' [1, 2] {'key': 'value}  {1} ('1')
# False : 0  ''  []  {}  () None
# print(bool(0))
# print(bool(12312))
# print(bool([0]))
# print(bool([]))
# print(bool(''))

# print(10 < 5)
# print(4 == 4)
# print(bool(False))
# print(bool(None))

# x = 100.321654
# print(isinstance(x, str))

# + - * /  %  **  //

# print(18/3)
# print(18//3)
#
# print(14 % 2 == 0)

# a = 10
# a = a + 1
# a += 1
# a -= 1
# a *= 2
# #########################################
# ==  !=  >  <  >=  <=
# a = 10
# b = 8
#
# print(a >= b)
# print(a != b)

# TDD test driven development
#
#
# a = 'salam'
# print('gmail' in a)
# print('gmail' not in a)

# a = 10
# b = 7
# print(a < b and a > 20)
# print(a < b or a > 20)

# and
#  0 0 -> 0
#  0 1 -> 0
#  1 0 -> 0
#  1 1 -> 1

# or
#  0 0 -> 0
#  0 1 -> 1
#  1 0 -> 1
#  1 1 -> 1

# a = ((10 < 5 and 5 == 5) or (5 < 9 and 10 > 11)) and 2 < 3
# # false - true - false - false
# # () / * - +
# a = 10 + 4 / (5 * 3) + 2
# #
# print(a)

# a = [1, 2, 3]
# b = a
# print(a is b)
# print(a == b)
# print(id(a))
# print(id(b))
# c = a[:]
# print(id(a))
# print(id(c))
# print(a is c)
# print(a == c)
# ##############################################
# if -  condition

# a = 10
# b = 7
#
# phone_number = '0'
#
# def validate_phone(x: str):
#     if x.startswith('+98') and len(x) == 13:
#         print('ok')
#         return True
#     elif x.startswith('0') and len(x) == 11:
#         print('ok')
#         return True
#     elif x.startswith('9') and len(x) == 10: # 09304857238 - +989304857238 - 9304857238
#         print('ok')
#         return True
#     else:
#         return False
#
#
#
# if phone_number:
#     print('okkkkkkkk')
#
# print('harchi')

import jdatetime
import datetime

print(datetime.datetime.now())
print(jdatetime.datetime.now())

