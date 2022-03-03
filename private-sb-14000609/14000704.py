# class Animal:
#     super_class_attr = 5
#
#     def __init__(self, parametr0=8):
#         self.parametr0 = parametr0
#
#     def walk(self):
#         return (f'{self.__class__.__name__}: Walking.......')
#
#     def breath(self):
#         return (f'{self.__class__.__name__}: Breathing.......')
#
# class ErtheAnimal:
#     pass
#
# class Dog(Animal, ErtheAnimal):
#
#     def __init__(self, parametr1, parametr0):
#         super().__init__(parametr0)
#         self.paramet1 = parametr1
#
#     def run(self):
#         return (f'{self.__class__.__name__}: Running.......')
#
#     def walk(self):
#         return (f'{self.__class__.__name__}:Dog Walking.......')
#
#
# class Sparrow(Animal):
#     def fly(self):
#         return (f'{self.__class__.__name__}: flying.......')
#
#     def breath(self):
#         return (f'{self.__class__.__name__}:Sparrow Breathing.......')
#
# dog = Dog(super_ins_attr=7)
# sparrow = Sparrow(8)
# print(dog.walk())
# print(sparrow.breath())
# print(dog.super_ins_attr)



# --------------------------------
# # import googletrans
# from googletrans import Translator
#
# translator = Translator()
# translator.translate('سلام')
# print('ok')