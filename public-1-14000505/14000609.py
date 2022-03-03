
# def decorator_func(a_func):
#     def wrapper():
#         print(' ghable func')
#         a_func()
#         print('baade func')
#     return wrapper
#
# @decorator_func
# def test_func():
#     print('ye chizi')

# test_func()

# a = decorator_func(test_func)
# a()

# def multy_in2(func):
#     def wrapper(*args, **kwargs):
#         return func(*args) * 2
#     return wrapper
#
#
# @multy_in2
# def sum2(a, b):
#     return a + b

# z = sum2(3, 4)
# v = multy_in2(sum2)
# x = v(3, 4)
# print(z)

# def formatting(lowercase=False):
#     def formating_decorator(func):
#         def wrapper(text=''):
#             if lowercase:
#                 func(text.lower())
#             else:
#                 func(text.upper())
#         return wrapper
#     return formating_decorator
#
#
# @formatting(lowercase=True)
# def printing(text):
#     print(text)
#
# @formatting(lowercase=False)
# def printing2(text):
#     print(text)
#
# printing('ASDHASDK ASDK ASKD')
# printing2('aasd vcxcv ')

# -------------------------------------

# class Car:
#     charkh = 4
#     ayne = 2
#     motor = 1
#
#     def __init__(self, color, model):
#         self.color = color
#         self.model = model
#
#     def show_color(self):
#         return self.color

# z = [1, 2, 3]
# print(z.pop())

# a = Car(color='red', model=99)
# b = Car(color='blue', model=1400)
# print(id(a))
# print(id(b))
# print(isinstance(a, int))
# print(a.color)
# print(b.color)
# c = b.show_color()
# print(c)

# instance method, class method, static method

# class Sample:
#     test = 0
#
#     def __init__(self, text='*'):
#         self.text = text
#
#     def instance_method(self):
#         return self.text * 10
#
#     @classmethod
#     def class_method(cls):
#         pass
#
#     @staticmethod
#     def static_method():
#         pass
#
# a = Sample()
# print(a.instance_method())

# class Student:
#     school_name = "my_school"
#     test = 10
#
#     def __init__(self, fname, lname):
#         self.name = fname
#         self.lname = lname
#
#     @classmethod
#     def show_school_name(cls):
#         print(cls)
#         return f'school name is: {cls.school_name}'
#
#     @staticmethod
#     def info():
#         return f"this is a school class "
#
# print(Student.show_school_name())
# print(Student(fname='test', lname='test2').show_school_name())


# class Animal:
#     hands = 2
#     def walk(self):
#         print(f'{self.__class__.__name__}: walking!!!')
#
#     def breath(self):
#         print(f'{self.__class__.__name__}: breathing!!!')
#
# class Dog(Animal):
#     def walk(self):
#         print(f'{self.__class__.__name__}: dog walking!!!')
#
# class Bird(Animal):
#     def fly(self):
#         print(f'{self.__class__.__name__}: flying!!!')
#
#
# dog = Dog()
# bird = Bird()
#
# # print(dog.run())
# print(dog.walk())
#
# print(bird.fly())
# print(bird.walk())

# class SuperClass:
#     super_class_attr = {'one': 1, 'two':2}
#
#     def __init__(self, parm1, parm2):
#         self.parm1 = parm1
#         self.parm2 = parm2
#
# class SubClass(SuperClass):
#     sub_class_attr = {'three': 3, 'four': 4}
#
#     def __init__(self, parm1, pram2, parm3):
#         super().__init__(parm1, pram2)
#         self.sub_parm2 = parm3
#
#     def instance_method(self):
#         print(self.sub_class_attr)
#
#     @classmethod
#     def class_method(cls):
#         print(cls.super_class_attr)
#
#
# a = SubClass(1 , 2, 3)
# print(a.parm1, a.instance_method(), a.class_method())

# class SuperClassA:
#     def __init__(self, a1, a2):
#         self.a1 = a1
#         self.a2 = a2
#
# class SuperClassB:
#     def __init__(self, a3):
#         self.a3 = a3
#
# class SuperClassC:
#     def __init__(self, a4):
#         self.a4 = a4
#
# class SuperClassD(SuperClassA, SuperClassB, SuperClassC):
#     def __init__(self, a1, a2, a3, a4, a5, a6):
#         SuperClassA.__init__(self, a1, a2)
#         SuperClassB.__init__(self, a3)
#         SuperClassC.__init__(self, a4)
#         self.a5 = a5
#         self.a6 = a6

# print(isinstance(sub, A))
# print(isinstance(sub, B))
# print(isinstance(sub, C))
# print(isinstance(sub, object))

# def sum_in2(a) -> int:
#     return a + 5
# user_input = input("enter a number: ")
# try:
#     adad = int(user_input)
# except:
#     print('somthing is wrong')
# else:
#     print(sum_in2(adad))
#     print('ok')
# finally:
#     print('finaly')

# def sum_divide(a, b):
#     try:
#         sum = a + b
#         div = sum / a
#         return sum, div
#     except Exception as exc:
#         print(exc)
    # except (TypeError, ZeroDivisionError) as func_eror:
    #     print(f'{func_eror} is happening because: a is {a} and b is {b}')
    # except:
    #     print('other error')

# print(sum_divide(2,4))
# sum_divide(2,'test')
# sum_divide(0,4)
# sum_divide(True,4)
# sum_divide([0],4)
# sum_divide('5','a')

# def sum_in2(a):
#     if not isinstance(a, int):
#         raise TypeError(f'type error rising because a is: {type(a)}')
#     return a + a
#
# b = sum_in2(5)
# print(b)
# c = sum_in2('a')
# print(c)

# class NegativeValueError(Exception):
#
#     def __init__(self, value, message=f'value is negative'):
#         self.value = value
#         self.message = message
#
#     def __str__(self):
#         return f'ERROR: value is {self.value} -> message is {self.message}'
#
# def plus(a):
#     if a < 0:
#         raise NegativeValueError(a)
#     return a + a
#
# try:
#     print(plus(5))
#     plus(-1)
#     # print(plus('a'))
# except NegativeValueError as err:
#     print(str(err), 'test')
# except:
#     print('other error')

class Student:
    school_name = "my_school"
    test = 10

    def __init__(self, fname, lname):
        self.name = fname
        self.lname = lname

    @classmethod
    def show_school_name(cls):
        print(cls)
        return f'school name is: {cls.school_name}'

    @staticmethod
    def info():
        return f"this is a school class "

    def setattr(self, value):
        self.value = value

    def __setattr__(self, *args, **kwargs):
        return 'hello'

    def __repr__(self):
        return 'test'

import math

student = Student(fname='test', lname='harchi')
# student.__delattr__('lname')
# print(student.lname)
print(student.__dir__())
# student.__setattr__('check', 20)
print(student.__setattr__())
# print(student.check)
# print(student.__getattribute__('abc')) # student.abc
