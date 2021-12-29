x = 5
y = 6
# + - * / // % -x **

# import math
# import numpy
#
# print(abs(-45))
# print(math.sqrt(25))
# print(max([1, 2, 3]))
# print(pow)

# int float complex
# print(3j + 2)
# print(type(4.0))

# a = 'print(3)'
# eval(a)
# print(10_000_000_000)
# print(1e6)
# a = 5
# result = f'1e{a}'
# print(float(result))
# eval(result)

# print(bool(''))
# ' ' 1 6 True {1, } (1, )
# '' 0 False {} () []
# print(10 < 8)
# print(10 == 10)
# a = 100
# print(isinstance(a, str))

# a += 100 # a = a + 100
# -= *= /=

# print(7 == 7) # ==(mosavi) <= >= !=(na mosavi) < >
# v = 'abc'
# print('z' not in v)

# ----------------------------------
# a = 7
# b = 10

# def getting_input():
#     return input('enter your name: ')
#
# name = getting_input()
#
# if name.isdigit():
#     print(' wrong input')
#     getting_input()
# elif a < b:
#     print('a equal b')

# a = 5
# b = 50
# if a < b or a == 5 and b < 20:
#     print('a lt b and is  5')
# else:
#     print('a ge b')

# print('a is b') if a == b else print('a ge b')
# 0  and  0 -> 0
# 0  and  1 -> 0
# 1  and  0 -> 0
# 1  and  1 -> 1

# 0  or  0 -> 0
# 0  or  1 -> 1
# 1  or  0 -> 1
# 1  or  1 -> 1

# -------------------------------------------
# def validate_phone_number(phone_number):
#     if phone_number.startswith('+98'):
#         print('phone number is valid')
#         if phone_number[3:5] == '912':
#             print('mci')
#             return True
#     else:
#         print('wrong input')
#         return False
#
# user_input = input('enter phone number: ')
# if validate_phone_number(user_input):
#     print('phone number is valid')
# ---------------------

# def add(x, y=5, *args, **kwargs):
#     print(args)
#     print(kwargs['o'])
#     return x + y
#
# print(add(56, 89, 90, 105, 205, z=6, f=9, o=10))
# print(add(x=5, y=6))
# print(add(x=8))
# print(add(x=1, y=6))
# print(add(x=4, y=2))


# def calculator(a, b, operator):
#     if operator == 'sum':
#         return a + b
#     elif operator == 'minus':
#         return a - b
#     elif operator == 'prod':
#         return a * b
#
# result = calculator(a=5, b=7, operator='prod')
# print(result)

count = 0

def ask_user(prompt):
    side = input(prompt)
    return int(side) if side.isdigit() else 0
    # side = input(prompt)
    # if side.isdigit():
    #     return int(side)
    # else:
    #     return 0

def calculate_area(length):
    return length ** 2

def calculate_area_cicle(length):
    pi = 3.14
    return

def show_menu():
    print('\n=================================')
    print('            WELCOME')
    print('1. Calculate the area of a square')
    print('2. Calculate the area of a Circle')
    print('3. Calculate the area of a Tri')
    print('4. Calculate the area of a Tri')
    print('0. Exit')
    print('=================================')

while True:
    show_menu()
    choice = ask_user('Please make your choice: ')
    if choice == 1:
        result = calculate_area(ask_user('Please enter a length in meters: '))
        print(f'\nThe area of the square is {result} square meters')
        count += 1
    elif choice == 2:
        print(
            f'You\'ve made {count} area calculations. Thanks for using this program')
        break
    else:
        print('\n --> Incorrect choice. Please try again. <--')
