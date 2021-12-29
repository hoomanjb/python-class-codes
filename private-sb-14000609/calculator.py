# class Calculator:
#
#     def __init__(self, adad_aval, adad_dovom):
#         self.adad_aval = adad_aval
#         self.adad_dovom = adad_dovom
#
#     def sum(self):
#         return self.adad_aval + self.adad_dovom
#
#     def sub(self):
#         return self.adad_aval - self.adad_dovom
#
#     def divide(self):
#         return self.adad_aval / self.adad_dovom
#
#     def prod(self):
#         return self.adad_aval * self.adad_dovom
#
#
# def getting_input(text):
#     return input(text)
#
# while True:
#     try:
#         a = float(getting_input('enter a number 1: '))
#     except Exception as exc:
#         print('somthing is wrong 1')
#         continue
#     try:
#         b = float(getting_input('enter a number 2: '))
#     except:
#         print('somthing is wrong 2')
#         continue
#
#     calculator = Calculator(adad_aval=a, adad_dovom=b)
#     print(calculator.sum())
#     print(calculator.sub())
#     print(calculator.prod())
#     print(calculator.divide())

a = 5
b = 2
try:
    print(a/b)
except ZeroDivisionError as exc:
    print('ZeroDivisionError rokh dade')
except ValueError as exc:
    print('ValueError rokh dade')
except Exception as exc:
    print('yechizi dg rokh dade')
else:
    print(' okeye khataii ndashtim')
finally:
    print('harchi shod inja miay')