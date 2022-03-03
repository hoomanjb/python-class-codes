# def my_func(a, b=True):
#     return a, b
#
#
# x, z = my_func(2)

# a , *b, c = 1 ,2 ,3 ,4 ,5

# def my_func(a: int, b: int, *args, **kwargs) -> float:
#     a = args
#     b = kwargs
#     result = a + b
#     return float(result)
#
# a = 1
# b = 4
# v = my_func(a=1, b=5, operator='/')

# print(v)

# b = lambda a: a + 10
# print(type(b))
# print(b(5))
# z = lambda a, b: a * b
# print(z(5,6))

# ---------------------------------------------

# def char_changer(string, char):
#     # tesssta -> tesss$a
#     result = string
#     temp_list = []
#     for index, item in enumerate(string):
#         if item not in temp_list:
#             temp_list.append(item)
#         else:
#             if item == char:
#                 result = string[:index] + '$' + string[index+1:]
#     return result

# a = 'abc' # dec
# b = 'def' # abf
# def char_changer(a, b):
#     new_a = b[:2] + a[2:]
#     new_b = a[:2] + b[2:]
#     return new_a + '  ' + new_b
#
# print(char_changer(a, b))

# a = ['hooman','aaaaaaaaaaaaaaaa', 'tehran', 'tesssst', 'test']
#
# def find_longest_word(a):
#     temp_list = []
#     for item in a:
#         temp_list.append((len(item), item)) # [(4, test),(),(),(7, tesssst)]
#     temp_list.sort()
#     return temp_list[-1][0], temp_list[-1][1]
#
# print(find_longest_word(a))
# a = 'https://test/python-exercises/string'
#
# print(a.rsplit('/', 1)[1])
# print(a.rsplit('-', 1))
# print(a.split('://'))


# def word_counter(text: str):
#     result_dict = dict()   #result_dict = {}   #{'test': 1}
#     words = text.split()   #split -> ' '
#
#     for word in words:
#         if word in result_dict:
#             result_dict[word] += 1  # {'test': 1}
#         else:
#             result_dict[word] = 1
#
#     return result_dict
#
# print(word_counter('test hello world test anisa good test anisa world hello ok'))

