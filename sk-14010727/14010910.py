# my_list = ['apple', 'test', 'hello']
# my_list_iter = iter(my_list)
#
# print(next(my_list_iter))
# print(next(my_list_iter))
# print(next(my_list_iter))


# my_list = ['apple', 'test', 'hello']
#
#
# class PrintNumberIter:
#     def __init__(self, max_number):
#         self.max = max_number
#
#     def __iter__(self):
#         self.num = 0
#         return self
#
#     def __next__(self):
#         if self.num >= self.max:
#             raise StopIteration
#         self.num += 1
#         return self.num
#
# print_obj = PrintNumberIter(10)
# print_obj_iter = iter(print_obj)
# print(next(print_obj_iter))
# print(next(print_obj_iter))
# print(next(print_obj_iter))
# print(next(print_obj_iter))
# print(next(print_obj_iter))
# print(next(print_obj_iter))
# print(next(print_obj_iter))
# print(next(print_obj_iter))
# print(next(print_obj_iter))
# print(next(print_obj_iter))
# print(next(print_obj_iter))


#
# class DoubleIt:
#     def __init__(self):
#         self.start = 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.start *= 2
#         return self.start
#
#     __call__ = __next__
#
#
# dd = iter(DoubleIt(), 16)
#
# for item in dd:
#     print(item)


# class Counter:
#     def __init__(self):
#         self.current = 0
#
#     def __getitem__(self, index):
#         if isinstance(index, int):
#             self.current += 1
#             return self.current
#
#     def __iter__(self):
#         return self.CounterIterator(self)
#
#     class CounterIterator:
#         def __init__(self, counter):
#             self.__counter = counter
#
#         def __iter__(self):
#             return self
#
#         def __next__(self):
#             self.__counter.current += 1
#             return self.__counter.current

# #######################################################

# OOP Object Oriented Programming
# شی گرایی


# class Car:
#     # class attr
#     wheel = 4
#     engine = 1
#
#     # instance attr
#     def __init__(self, color, model='x0'):
#         self.color = color
#         self.model = model
#
#     # instance method
#     def show_color_and_model(self):
#         return f'your color is {self.color} and your model is {self.model}'
#
#     def __yechizi(self):
#         pass
#
#     # static method
#     @staticmethod
#     def show_welcome_msg():
#         return 'Welcome Sir!'
#
#     # class method
#     @classmethod
#     def show_class_attr(cls):
#         return cls.wheel
#
#
#
#
# car = Car(color='black', model='x')
# car2 = Car(color='green', model='x2')
# car3 = Car(color='red')
#
# print(car.wheel)
# print(car2.wheel)
# print(car3.wheel)
#
# print(car.color)
# print(car2.color)
# print(car3.color)
#
#
# print(car.model)
# print(car2.model)
# print(car3.model)
#
# print(car.show_color_and_model())
# print(car.show_welcome_msg())
#
#
#
# print(Car.show_welcome_msg())

# class Animal:
#
#     hearth = 1
#
#     def breathing(self):
#         return 'Animal breathing .....'
#
#     def eating(self):
#         return 'Animal eating .....'
#
# # parent pedar base
# # child subclass
#
# class SeaAnimal(Animal):
#     # over rid kardan method haii k dar class parent sakhte shode
#     def breathing(self):
#         return 'SeaAnimal breathing .....'
#
#     def swiming(self):
#         return 'SeaAnimal swiming .....'
#
#
# class LandAnimal(Animal):
#
#     def breathing(self):
#         return 'LandAnimal breathing .....'
#
#     def walking(self):
#         return 'LandAnimal walking .....'
#
#
# fish = SeaAnimal()
#
# lion = LandAnimal()
#
# print(fish.breathing())
# print(lion.breathing())
# print(lion.walking())
# print(fish.swiming())


# ####################################################

# class Human:
#
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#
#     def walking(self):
#         return 'Human Walkin'
#
#     def talking(self):
#         return 'Human Talking'
#
#
# class Man(Human):
#
#     def __init__(self, first_name, last_name, age):
#         super().__init__(first_name, last_name)
#         self.age = age
#
#     def walking(self):
#         return 'Man Walking .....'
#
#
# human = Human(first_name='ali', last_name='taghi')
#
# man = Man(first_name='ali', last_name='taghi', age=40)

# #######################################
import datetime
from datetime import datetime

print(datetime.now())

import adder
from adder import Calculator

cal = Calculator(7, 10)
print(cal.adder_funcation())
print(cal.divide_funcation())
print(cal.prod_funcation())
print(Calculator.sub_func(8, 9))


