# while , for
# continue, break
# a = 0
# while a < 5 or a == 5:
#     print(f'a is {a}')
#     b = a + 2
#     print(f'b is {b}')
#     if b == 4:
#         a += 1
#         continue
#     c = a * 3
#     if c == 9:
#         print('break calling')
#         break
#     print(f'c is {c}')
#     print('#' * 10)
#     a += 1
# else:
#     print('other')
# -------------------------------------------
# a = [1, 2, 3, 4]
# for item in a:
#     if item == 2:
#         continue
#     if item == 4:
#         break
#     print(item)
# ---------------------------------------------
# a = [1 ,2 ,3 ,4]
#
# b = [item + 2 for item in a]
# print(a)
# print(b)
# a = 'test'
# for char in a:
#     print(char)
# -------------------------------------------
# x = list((1, 2, 3, 4,5))
# a = [1, 2 ,3 ,4, 'test2', True, False, [5 ,6, 'test'], [7, 8,[9, 10,[11]]]]
# print(a[8][2][2][0])
# print(a[4][2])
# if 'test' in a[7]:
#     print('test is exsit')
# # print('else')
# a[0] = 20
# print(a)
# print(x)
# a = [0, 1, 2, 3, 4, 'test', True, False, [5 ,6, 'test'], [7, 8,[9, 10,[11, 'test']]], [23, 24]]
# b = [23, 24]
# a.append(b)
# a.extend(b)
# a.insert(1, 45) # insert(index, object)
# print(a[9][2].index(10))
#{'userName: felan, password: 1123'}
# a[9][2][2].insert(0, 25)
# print(a)
# z = [0, 1, 2, 3, 4, 'test', True, False, [5, 6, 'test',[1, 2]], 'test', 6]
# # print(a.count(4))
# v = 1
# isinstance(v, int)
# counter = 0
# for item in z:
#     if isinstance(item, list):
#         for i in item:
#             if isinstance(i, list):
#                 for j in i:
#                     if j == 'test':
#                         counter += 1
#             if i == 'test':
#                 counter += 1
#     if item == 'test':
#         counter += 1
# print(counter)

# z = [0, 1, 2, 3, 4, 'test', True, False, [5, 6, 'test',[1, 2]], 'test', 6]
# z.pop(2) # default last by index
# z.clear()
# print(z)
# z.remove('test') # remove by item
# print(z)
# f = [2, 3, 1, 6, 8, 0]
# x = ['a', 'A', 's', 'z', 'Z', 'V', 'TEST']
#
# z.reverse()
# x.sort(key=str.lower, reverse=True)
# print(x)
# b = [1, 2, 3 ,4 ,5 ,6 ,7, 10, 12, 14]
# a = [item for item in b if item%2 == 0]
# print(a)


