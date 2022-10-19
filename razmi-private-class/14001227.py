#23. Write a Python program to combine values in python list of dictionaries.
# Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
# Expected Output: Counter({'item1': 1150, 'item2': 300})

# my_dict = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
# keys = []
# value_keys = []
# key_value_list = []
# result = {}
#
# for item in my_dict:
#     for key in item.keys():
#         if key not in keys:
#             keys.append(key)
#
# for key in keys:
#     if key == 'item':
#         for item in my_dict:
#             if item[key] not in value_keys:
#                 value_keys.append(item[key])
#
# for key in value_keys:
#     for item in my_dict:
#         if key in item.values():
#             value = item['amount']
#             if key in result:
#                 value = result[key]
#                 value += item['amount']
#             result.update({key: value})
#
# print(result)

# for i in key_value_list:  # in c
#     e=str(c[i][1])
#     f=int(c[i][0])
#     for j in range(len(c)):
#             g = str(c[j][1])
#             h= int(c[j][0])
#             if e==g and i!=j:
#                 s=f+h
#                 print({e:s})
#             elif e!=g and i!=j:
#                 print({e:f})
# #########################################################################
# class Car:
#     # class attr
#     wheel = 4
#     engine = 1
#
#     # instance attr
#     def __init__(self, color='black', name_db=''):
#         self.color = color
#
#     # instance method
#     def get_color(self):
#         return self.color
#
#     @staticmethod
#     def driving(name):
#         return f'{name} is Driving........'
#
#     @classmethod
#     def get_wheel(cls):
#         return cls.wheel
#
#
# pride = Car(color='red')
#
# benz = Car()
#
# print(pride.color)
# print(benz)
# print(pride.get_color())
# print(benz.get_color())
# print(pride.driving(name='hooman'))

# class Person:
#     def __init__(self, fname, lname):
#         self.fname = fname
#         self.lname = lname
#
#     def get_name(self):
#         return f'My name is {self.fname} {self.lname}'
#
#     def get_info(self):
#         return ''
#
#
# class BoyStudent(Person):
#     def __init__(self, age, fname, lname):
#         super().__init__(fname, lname)
#         self.age = age
#
#     def get_info(self):
#         return 'this is a BoyStudent object for Boys'
#
#     def __repr__(self):
#         return 'man az class Boy Student hastam'
#
#
# class GirlStudent(Person):
#     def __init__(self, age, fname, lname):
#         super().__init__(fname, lname)
#         self.age = age
#
#     def get_info(self):
#         return 'this is a BoyStudent object for Girls'
#
# person = Person(fname='ccccc', lname='gggg')
# print(person)
#
# boy = BoyStudent(age=20, fname='hooman', lname='javan')
# print(boy)
# print(boy.__class__.__base__)
# print(boy.get_name())
# print(boy.get_info())
#
#
# girl = GirlStudent(age=30, fname='hhhh', lname='aaaa')
# print(girl)
# print(girl.get_name())
# print(girl.get_info())

# ####################################################
# ERROR HANDLING
try:
    a = 3
except Exception as ex:
    print('ye moshkeli hast')
    print(ex)
else:
    print('success')


print('harchizi')

# request (rest, api) , database, excel, regex, os sys , ftp ssh ,