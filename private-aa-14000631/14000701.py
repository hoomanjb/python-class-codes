# break, if while for

# help('keywords')

# name = 'hooman he1$llo world'
#       012345
name2 = "hooman"
name3 = '''hooman'''
a = str(4)
# print(name[-1])
# name[start:end:step]
# print(name[2:9:2])
# print(name[::-1])

# print(type(len(name)))
# name = 'hOOMan-he1$llo-world-test'
# [1, 2, 3]
# print(name.split(sep='$'))
# print('h' in name) # in
# print(name.count('hooman'))
# lower_name = name.lower()
# print(name)
# print(lower_name)
a = 'hello'
b = ' world'
c = (a + b) + ' ' * 5  # () * / + -

name = 'hOOMan-he1$llo-wor$ld-t$est'
# print(c)
# print(name.replace('M', 'Z'))
# print(name.index('$', 11, 15)) # Wrong
# print(name.find('h', 9))
# print('         hello'.strip())
# print('hello        '.rstrip())
# print('123141234'.isalnum())
# print(name.islower())
# print('apple'.capitalize())
# print(name.startswith('z'))

# template_text = '{name:*^10.10} welcome  {age:.2f} hello {dec:-}'
# text = template_text.format(name='aliii',
#                             age=52.123123123,
#                             dec=-54)
# print(text)
# {name:[[fill]align][sign][#][0][width][,]
# [.precision][type]}
a = 'hooman'
b = 30.4
c = 'IR'
fill = '@'
align = '^'
# print(f'1-name: {a:{fill}{align}10.10}  2-age: {b} 3-country: {c}')

# ----------------------------
import math

side = input('plz enter a number: ')
if side.isdigit():
    shape = input('plz enter a shape:1)a, 2)b ')
    if shape == '1' or shape == 'a':
        result = math.pow(int(side), 3) # addad**3
    elif shape == '2' or shape == 'b':
        result = math.pow(int(side), 3) // (6 * math.sqrt(2)) # 6 * jazr2
    else:
        result = 'wrong shape'
    print(f'your side is {side} and your result is: {result}')
else:
    print('wrong input')








