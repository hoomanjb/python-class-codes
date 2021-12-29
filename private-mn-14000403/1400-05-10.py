# def getting_input():
#     return input("enter your words: ")
#
# def check_length(my_list: list, name='ali', *args, **kwargs) -> str:
#     return max(my_list)
#
# if __name__ == '__main__':
#     user_input = getting_input()
#     words = user_input.split()
#     result = check_length(words, 'sdf', 'sdfsf', 'sdfsdf', test='ali', test2='ali2')
#     print(result, len(result))

# def func1(a):
#     return lambda b: a + b

# if __name__ == '__main__':
    # test = lambda a, b: a + b
    # print(test(5, 7))
    # test = func1(5)
    # print(test(6))
    # print(test(8))
    # print(test(21))

# if __name__ == '__main__':
#     my_dict = {'key1': 12, 'key2': 'test',
#                'key3': [1, 2, 3], 'key4': (1, 2, 3,),
#                'key5': {1, 2, 3}, 'key6': True}

# x = 'test'
# y = 'test1'
# print(type(x))

# 'user_input'.split()

# class Human:
#     """
#     this is a Human Class
#     """
#     hands = 2
#     feet = 2
#     eye = 2
#     nose = 1
#
#     def __init__(self, jensiat='mard'):
#         self.jensiat = jensiat
#
#     def tanfos(self):
#         return 'nafas keshidan'
#
#     def rah_raftan(self):
#         return 'rah raftan'
#
#     def __repr__(self):
#         return f'jensiat is {self.jensiat}'
#
# mard = Human('mard')
# zan = Human('zan')
#
# print(mard.jensiat)
# print(zan.jensiat)
# print(mard)
# print(zan)

# class Car:
#     wheel = 4
#     engine = 1
#     ayne = 2
#
#     def __init__(self, rang, model=1400):
#         self.rang = rang
#         self.model = model
#
#     def move(self):
#         return 'harekat'
#
#     def __repr__(self):
#         return f'in objecti k sakhti rangesh {self.rang} , modelesh  {self.model}'
#
#
# car1 = Car(rang='sabz')
# car2 = Car(rang='ghermez', model=1399)
# print(car1)
# print(car2)
# print(car2.rang)
# car1.__setattr__('cheragh', 4)
# car1.cheragh = 4
# print(car1.cheragh)
# print(car1.__getattribute__('cheragh'))
# print(car1.__sizeof__())
# print(car1.__class__)


# class Square:
#
#     def __init__(self, side):
#         self.set_side(side)
#
#     def set_side(self, side):
#         if side == 0:
#             self.side = 1
#         else:
#             self.side = side
#
#     def area(self):
#         return self.side ** 2
#
#     def prime(self):
#         return self.side * 4
#
#     def get_side(self):
#         return self.side
#
# moraba_aval = Square(side=5)
# print(moraba_aval.area())
# print(moraba_aval.prime())
# print(moraba_aval.get_side())
#
# moraba_aval.set_side(6)
# print(moraba_aval.area())
# print(moraba_aval.prime())
# print(moraba_aval.get_side())


class Converter:
    def __init__(self, yard):
        self.yard = yard

    def yard_to_metr(self):
        return self.yard / 1.196