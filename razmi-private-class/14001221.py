# [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

# def last(n: list) -> list:
#     return n[-1]
#
# a = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# print(sorted(a, key=lambda x: x[-1]))
#
# a = 'Hi hello Hi okj[oj[pl hello'
# b=a.split()
# c=[]
# for i in b:
#     if i not in c:
#         c.append(i)
#         print(c)
#     else:
#         print('Find Reapeted word')
#         break
# my_list = [3, 4, 1, 9, 9, 10, 23, 90]
# #############################################
# DRY

# def my_function():
#     return 'hello'
#
# print(my_function())

# def my_function_client(name: str, new_parametr: bool = None, age: int = 10, phone: int = 123) -> str:
#     # request -> str
#     return name
#
# # print(my_function(name='hooman', new_parametr=True))
#
# def my_function_sever(*args, **kwarg):
#     """
#     :param args: baraye positional args
#     :param kwarg:
#     :return: True
#     """
#     name = 100
#     print(args)
#     print(kwarg)
#
# my_function_sever(1, 4, 5, 7, 'hello', 'world', [6, 9], hooman='20', age=100, phone=123)
#
# name = '20'
# name = 'hello'
# name = True

# #################################
my_dict = {'name': 'hooman', 'age': 20, 1: ['hello', 'world']}
# print(my_dict['name'])

# print(my_dict.get('asdasd', 20))

# print(my_dict.keys())
# print(my_dict.values())
# print(my_dict.items())
# for item in my_dict.items():
#     print(item)

# if 'hooman' in my_dict.values():
#     print('exist')

# a = {'test': 100}
#
# my_dict.update(a)
# print(my_dict)
# my_dict.pop('name')
# print(my_dict)
# my_dict.clear()

# #######################################
a = lambda b: b + 10
print(a(5))
# #########################################

class Animal:
    heart = 1
    brain = 1

    def __init__(self, name):
        self.name = name

    def breath(self):
        a = self.name
        pass

    def walk(self):
        pass

    def eat(self):
        pass

cat = Animal(name='yechizi')
print(cat.name)
dog = Animal(name='2chizi')
print(dog.name)
fish = Animal(name='3chizi')
print(fish.name)




