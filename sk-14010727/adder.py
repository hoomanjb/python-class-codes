
class Calculator:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def adder_funcation(self):
        return self.x + self.y

    def prod_funcation(self):
        return self.x * self.y

    def divide_funcation(self):
        return self.x / self.y

    @staticmethod
    def sub_func(x, y):
        return x - y