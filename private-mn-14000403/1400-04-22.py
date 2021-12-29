# user_input = input("enter your input: ")
# # ['2', '2', 'ali', '2', '3', 'ali']
# user_list = user_input.split()
# result = []
# for index, item in enumerate(user_list):
#     if item not in result:
#         result.append(item)
#         print(index, ' ', item)
#     else:
#         continue
# print(result)

# my_tuple = tuple((2, 3, 5, 6, 4))
# my_tuple2 = (2, 3, 4, 5)
# print(type(my_tuple))
# print(type(my_tuple2))
# if 2 in my_tuple2:
#     print("2 in my_tuple")
# else:
#     print("wrong")
#
# my_tuple = (2, 3, 4, 5)
# print(my_tuple[2])
#
# temp = list(my_tuple)
# print(my_tuple)
# print(temp)
# temp[2] = 'hooman'
# my_tuple = tuple(temp)
# print(temp)
# print(my_tuple)
# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
# (*a, b, c) = fruits
# print(a)
# print(b)
# print(c)
# my_set = {"apple", "apple", "apple", "banana", "cherry", "strawberry", "raspberry"}
# for item in my_set:
#     print(item)
# my_set.pop()
# my_set.add('hooman')
# my_set.add('apple')
# my_set.remove('apple')
# my_set.discard('apple')
# my_set.clear()
# print(my_set)

# my_dict = {"name": "hooman",
#            "last_name": "javanbakht",
#            "birth_Date": 1990,
#            "year": {2021, 2022}}

# print(type(my_dict))
# print(my_dict["last_name"])
# print(my_dict.get('last_name', 'Wrong'))
# print(len(my_dict))
# print(my_dict.values())
# print(my_dict.keys())
# print(my_dict.items())
# my_dict['year'] = 2020
# print(my_dict)
# test = my_dict.items()
# for key, value in test:
#     print(type(key), " ", type(value))

# ------------------------------------------- #

# def my_function():
#     return 'salam'
#
# result = my_function()
# print(result)

# def my_function(user_input1, user_input2):
#     return user_input1 + user_input2
#
# result = my_function(5, 9)
# print(result)

# def my_function(name: str, last_name='salam', year=2021):
#     return {"name": name, "last_name": last_name, "year": year}
#
# result = my_function(name='hooman', last_name='bybye')
# print(result)

# def my_function(name, *args):
#     new_list = list(args)
#     return args
# result = my_function('hooman', 'javan', 2021)

# def my_function(name, *args, **kwargs):
#     return kwargs
# result = my_function('test',2055 ,name='hooman', last_name='javan', year=2021)
# print(result)
# -----------------------------------
# def add(x, y):
#     return x + y
#
# def mines(x, y):
#     return x - y
#
# def do_twice(func1, func2, x, y):
#     new_x = func1(x, y)
#     new_y = func2(x, y)
#     return func1(new_x, new_y)
#
# print(do_twice(add, mines, x=4, y=5))

def getting_input():
    user_input = input("enter: ")
    return user_input

def splitting_user_input(vorodi: str):
    my_list = vorodi.split()
    return my_list

def remove_duplicate_value(liste_jadid) -> list:
    my_set = set(liste_jadid)
    return list(my_set)

def main():
    user_input = getting_input()
    my_splitted_list = splitting_user_input(user_input)
    result = remove_duplicate_value(my_splitted_list)
    print(result)

main()