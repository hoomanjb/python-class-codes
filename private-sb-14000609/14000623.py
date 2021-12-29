# GUI, tkinter
# pandas ,
# sqlite3 postgres mysql
# requests
# regex

# ab ca er da

# def first_repeated_word(text):
#     temp = set()
#     words = text.split()
#     for word in words:
#         if word in temp:
#             return word
#         else:
#             temp.add(word)
#     return None
#
# print(first_repeated_word('ab ca ab ca'))
# print(first_repeated_word('ab ca da ca'))

# p y t h o n
#
# def remove_spaces(text):
#     """
#     fghad remove kardane ye doone space
#     :param text:
#     :return:
#     """
#     text = text.replace(' ', '')
#     return text
#
# print(remove_spaces('p y t h o n'))


# def remove_duplicate_char(word):
#     result = ''
#     for char in word:
#         if char in result:
#             continue # break
#         else:
#             result += char
#     return result
#
# print(remove_duplicate_char('pythonnnnnnn'))

# def sum_digits_string(text):
#     sum = 0
#     for char in text:
#         if char.isdigit():
#             adad = int(char)
#             sum += adad
#     return sum
#
# print(sum_digits_string('123123asdfsdf123'))


# testtt  testdgs
# set list str int float bool dict
# def uncommon_chars_concat(s1, s2):
#     set1 = set(s1)
#     set2 = set(s2)
#     common_chars = list(set1 & set2)
#     result = [ch for ch in s1 if ch not in common_chars] + [ch for ch in s2 if ch not in common_chars]
#     return ''.join(result) # acbd
#
# s1 = 'abcdpqr'
# s2 = 'xyzabcd'
# print(uncommon_chars_concat(s1, s2))


def charakter_seperation(text: str):
    result = {"lowercase": 0, "uppercase": 0, "numeric": 0, "special": 0}
    for char in text:
        if char.islower():
            result["lowercase"] += 1
        if char.isupper():
            result["uppercase"] += 1
        if char.isnumeric():
            result["numeric"] += 1
        if not char.isalpha() and not char.isdigit():
            result["special"] += 1
    return result
    # lowercase = 0
    # uppercase = 0
    # numeric = 0
    # special = 0
    # result = []
    # for char in text:
    #     if char.islower():
    #         lowercase += 1
    #     if char.isupper():
    #         uppercase += 1
    #     if char.isnumeric():
    #         numeric += 1
    #     if not char.isalpha() and not char.isdigit():
    #         special += 1
    # result.append(('lowercase', lowercase))
    # return result # [(lwoer , 5),(),()]


# print(charakter_seperation('asasd1231#$%#$SDFSDF'))


# def key_sort(item): # (1, 2)
#     return item[1]
#
# my_dict = {1: 2, 3: 9, 7: 8, 9: 10, 5: 6}
#
# sorte1 = sorted(my_dict.items(), key=key_sort ,reverse=True)
# print(sorte1)

# dic1 = {1: 10, 2: 20}
# dic2 = {3: 30, 4: 40}
# dic3 = {5: 50, 6: 60}
#
# dict4 = {}
# for item in (dic1, dic2, dic3):
#     dict4.update(item)
# print(dict4)

# x = {'name': 'test', 'age': 20}
# if 'name' in x.values(): #x.items() x.keys()
#     print('exist')

# x = int(input('enter a numer'))
# d = dict()
#
# for item in range(1, x + 1):
#     d[item] = item * item
#
# print(d)


# dic1 = {1: 10, 2: 20, 3: 50}
# print(sum(dic1.values()))

# keys = ['red', 'blue', 'green']
# values = [10, 20, 30]
#
# result = dict(zip(keys, values))
#
# print(result)

# {1: {2: {3: {4: {}}}}}
# a = [1, 2, 3, 4]
# new_dict = current = {}
# for item in a:
#     current[item] = {} # {1:}
#     current = current[item]
# print(new_dict)

# a = [1, 2, 3 , 4, 5, 6, 7, 8, 9, 10]
#
# for item in a:
#     print('*' * item)
# for item in a[::-1]:
#     print('*' * item)


# dic1 = {1: 10, 2: 20, 3: 50, 4: 60, 5: 70}
# print('{}  {}  {}'.format('key', 'val', 'ind'))
#
# for index, (key, value) in enumerate(dic1.items(), 1):
#     print(f'{key:^3}  {value:^3}  {index:^3}')


dict1 = {'Alex': ['subj1', 'subj2', 'subj3', ['sub7']], 'David': ['subj1', 'subj2']}

lis1 = [[1,2,3 ], [4, 5], [6, 7, 8, 9]]

a = map(len, lis1)
print(a)
print(sum(map(sum, lis1)))

print(sum(map(len, dict1.values())))
