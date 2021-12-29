def multiply(numbers): # [1, 2 ,3] (4 , 5, 6)
    total = 1
    for num in numbers:
        total *= num
    return total


# print(multiply(numbers=(1, 2, 3)))

def string_reverse(text):
    return text[::-1]

# print(string_reverse(text='123kjbhkjsk1j23hhhh'))

def factorial(n):
    if n == 0:
        return 1
    else:
        result = n * factorial(n-1)
        return result

# print(factorial(4))

def fibonachi(n): # 1,1,2,3,5,8
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        result = fibonachi(n-1) + fibonachi(n-2)
        return result

# print(fibonachi(6))
code = 'print("hello world")'

func = """
def add(x,y):
    return x + y
print(add(2,4))
"""
# exec(func)
# exec(code)

from math import pi

def circle_area(radios):
    return pi * radios**2

# print(circle_area(2))

# --------------------------------------------

# a = 5
# print(type(a))
# b = 'hello'
# c = 'world'
# print(type(b))
# print(b.lower())
# b = str()
# a = set()

def test():
    pass


#
# class MyClass:
#     pass
#
# a = MyClass()
#
# print(type(a))
# print(a.__dir__())
# print(a.__class__.__name__)

# class Car:
#     # class attr
#     charkh = 4
#     cheragh = 4
#     dar = 2
#     motor = 1
#
#     # instance method
#     def __init__(self, color, model='sport'):
#         # instance attr
#         self.color = color
#         self.model = model
#
#
#
# pride = Car(color='red')
# bmw = Car(color='blue', model='city')
#
# print(pride.charkh)
# print(pride.motor)
# print(pride.color)
# print(pride.model)
#
# print(bmw.charkh)
# print(bmw.motor)
# print(bmw.color)
# print(bmw.model)


class Animal:
    # class attr
    brain = 1
    eye = 2
    nose = 1

    def __init__(self, animal_type):
        #instance attr
        self.animal_type = animal_type

    #instance method
    def breath(self):
        return 'breathingggg'

    def walking(self): # self -> dastresi b hamechi
        return 'walkingggg'

    @staticmethod
    def my_static_method():
        return 'this is a static method'

    @classmethod
    def my_class_methode(cls): # cls -> dastresi b class attr faghad
        return cls.brain


mahi = Animal(animal_type='daryaii')
fil = Animal(animal_type='zamini')
print(mahi.breath())
print(fil.breath())
print(mahi.animal_type)
print(fil.animal_type)

# cal = Calculator(2, 3)
# print(cal.tafrigh())
# print(cal.zarb())
