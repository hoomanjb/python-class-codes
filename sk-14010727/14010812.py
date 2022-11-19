
# a = 10
# b = 20
# c = 40
# a, b, c = 10, 20, 40

# a = b = c = 10
# print(a)
# print(c)
# c = 20
# print(a)
# print(c)
# a = c
# print(a)
# c = 30
# print(a)
# print(c)
#
# print(id(a))
# print(id(c))
# c = 20
# print(id(a))
# print(id(c))
# int a = 20
# int c = 20

# a = 20
# c = 20
# print(id(a))
# print(id(c))

# #############################
# pep
# name = 'hooman'
# first_name_of_customers = 'hooman'
# name = 'hooman'
# نام = 'salam'
# print(نام)

# __name = '10'
# __name__ = '10'

# name = 'hooman'
# print(name.__class__)

# _print = 10
# ##################################
# a = "hello\n world"
# a = """
# hello
# world
# """
# print(a)
a = 'hello world'
# print(len(a))
# print(a[0])
# print('h' in a)  # operator
# print(a[:5])
# print(a[-1])
# print(a[len(a) - 1])
# print(a[:7:])
# print(a[:7:2])  # [start:end:step]
# print(a[::])
# print(a[-1:])
# print(a[-1::1])
# print(a[::-1])
# a = 1234654654
# b = str(a)
# a = int(b[::-1])
# print(a)

# a = str(3)
# print(a)
name = 'hooman@javanbakht'
# print(name.index('z'))  # Bad
# print(name.find('z'))

# print(name.count('a', 6, 10))

# print(name.upper())
# print(name.isupper())
# print(name)
# print(name.isdigit())
# a = '1234243423'
# print(a.isdigit())
# print(name.replace('z', 'b'))
# name = "ali10"
# print(name.isalpha())
# import uuid
# print(uuid.uuid4())

# print(name.split(sep='@'))

# name = 'hooman    '
# print(name.rstrip())
# print(name.lstrip())
# print(name.strip())

# a = 'hello '
# b = 'world'
# c = a + b
# print(c)
# print('#' * 50)

text = 'salam {0} be web site ma khosh amadid saat ham alan {1} ast'
print(text.format('hooman', '12:00'))

