
def count_words_items(words):
    count = 0

    for word in words:
        if len(word) > 2 and word[0] == word[-1]:
            count += 1
    return count

# temp_list = ['aba', 'ab', 'xyz', '12341', 'abcda', [1, 2, [4, 8]]]
# print(count_words_items(temp_list))
# print(len(temp_list))
# print(len('1234'))

# temp_list=[(1, 2), (4, 2), (5, 1), (1, 9), (2, 8), (3, 7)]
#
# def my_soretd_function(a):
#     return a[-1]
#
# print(sorted(temp_list))
#
# print(sorted(temp_list, key=my_soretd_function))

# temp_list = [1, 1, 1, 2, 3, 4, 5, 5, 5, 8, 9]
# print(list(set(temp_list)))
#
# def remove_duplicate_items(items):
#     result = []
#     for item in items:
#         if item not in result:
#             result.append(item)
#     return result
#
# print(remove_duplicate_items(temp_list))

a = []
# if not a:
#     print('a is empty')
# if len(a) == 0:
#     print(' a is empty')
# if a:
#     print(' a is true')
# else:
#     print('a is empty')
# if a[0] == a[-1]:
#     print('a is empty')

# 200 , 400, 500

# def long_words(n , items: list):
#     result = []
#     for item in items:
#         if len(item) > n:
#             result.append(item)
#     return result
#
# print(long_words(3, ['test', 'the', 'ok', 'hooman', 'anisa']))

# user_input = input('enter words: ')

# def my_split(my_stirng='test test', sep=' '):
#     result = []
#     temp_word = ''
#     length = len(my_stirng)
#     counter = 1
#     for char in my_stirng:
#         if counter == length:
#             if not char == ' ':
#                 temp_word += char
#             result.append(temp_word)
#         elif char == ' ' and (counter == 1 or counter == length):
#             pass
#         elif char != sep:
#             temp_word += char
#         else:
#             result.append(temp_word)
#             temp_word = ''
#         counter += 1
#     return result

# print(my_split('test1 test2 test3 test1'))
# print(my_split(' test1 test2 test3 test1'))
# print(my_split('test1 test2 test3 test1 '))
# print(my_split(' test1 test2 test3 test1 '))
# print(my_split('   test1 test2 test3 test1   '))


# my_list = user_input.split()
# print(long_words(3, my_list))


# def same_item(list1, list2):
#     result = False
#     for index1, x in enumerate(list1):
#         for index2, y in enumerate(list2):
#             if x == y:
#                 result = True
#                 return result, (index1, x), (index2, y)
#     return result, None, None
#
# print(same_item([1,2,3,4,5], [5,6,7,8,9]))

# a = [1,2 ,3 ,4 ,5]
# a.remove(2)
# del a[3]
# print(a)

# def remove_even_numbers(numbers):
#     # result = []
#     # for item in numbers:
#     #     if item % 2 != 0:
#     #         result.append(item)
#     result = [item for item in numbers if item % 2 != 0]
#     return result
#
# print(remove_even_numbers([2, 5, 6, 7, 9, 11, 15, 24]))

# import random
# # from random import shuffle, choice
#
# numbers = [1, 4, 6, 7, 8, 9, 2, 4, 6]
# random.shuffle(numbers)
# print(random.choice(numbers))
# print(numbers)

def square_values(items):
    # first5 = items[:5]
    # last5 = items[-5:]
    # result1 = []
    # result2 = []
    # for x in first5:
    #     result1.append(x**2)
    # for x in last5:
    #     result2.append(x**2)
    # return result1, result2
    return [x**2 for x in items[:5]], [x**2 for x in items[-5:]]

list1 = [1, 2, 3, 4, 5, 6, 7, 15, 16, 17, 18, 19, 20]
print(square_values(list1))
