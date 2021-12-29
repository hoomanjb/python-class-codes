# class Car:
#     wheel = 4
#     password = 123
#     engine = 1
#     ayne = 2
#
#     def __init__(self, rang, model=1400):
#         self.rang = rang
#         self.model = model
#
#     @staticmethod
#     def show_table():
#         table = 'cars'
#         return table
#
#     def move(self):
#         return 'harekat'
#
#     def user_request(self):
#         user_input = input('rookeshesh chi bashe?')
#         self.rookesh = user_input
#         self.__setattr__('rookesh', user_input)
#
#
#
#     def __repr__(self):
#         return f'1-in objecti k sakhti rangesh {self.rang} , modelesh  {self.model}'

    # def __str__(self):
    #     return f'2-in objecti k sakhti rangesh {self.rang} , modelesh  {self.model}'
    #

# a = input('enter number:')
# print(int(a) + 4)

# a = input('enter number:')
# try:
#     print(int(a) + 4)
#     # request = anisa
# except ValueError as e1:
#     raise Exception('gharar bood adad bedi chera gofti salam')
# except TypeError as e2:
#     print(e2)
#     print('net ghat shode')
# except Exception as e:
#     print(f'something wrong exception is {e}')
# else:
#     print('file dl shod')
# finally:
#     print('request zade shod, tamam')
#
#
# print('Im here')
# print('ok')

try:
    a = open('chert.txt','rt')
except:
    print('somthing is wrong')

print(a)


