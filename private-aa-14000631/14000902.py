class Circle:
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return self.pi * (self.radius ** 2)

    def get_prime(self):
        return (2 * self.pi) * self.radius

    def __repr__(self):
        return 'this is a object from Circle Class For getting area and prime'


# circle = Circle(radius=5)
#
# print(circle.get_area())
# print(circle.get_prime())


class PasswordManager:
    root_username = 'admin'
    root_password = '123'

    def check_password(self, user_name, password):
        return self.root_username == user_name and self.root_password == password

# user_name = input('enter username: ')
# password = input('enter password: ')
#
# pass_manager = PasswordManager()
#
# if pass_manager.check_password(user_name, password):
#     print('Correct')
# else:
#     print('Not Correct')

class CalculateTeacher:

    # def __init__(self, techer_id, fname, lname, hour, payment):
    #     self.teacher_id = self.set_id(teacher1)

    def set_id(self, teacher_id):
        self.teacher_id = teacher_id
    def set_firstname(self, teacher_firstname):
        self.teacher_firstname = teacher_firstname
    def set_lastname(self, teacher_lastname):
        self.teacher_lastname = teacher_lastname
    def set_time(self, teacher_time):
        self.teacher_time= teacher_time
    def set_payment(self, teacher_payment):
        self.teacher_payment = teacher_payment
    def set_calpayment(self):
        self.teacher_calpayment = self.teacher_time * self.teacher_payment

    def __repr__(self):
        return f'teacher {self.teacher_firstname} {self.teacher_lastname} with id {self.teacher_id}' \
               f'working {self.teacher_time} hours and payment is {self.teacher_calpayment}'

teacher1 = CalculateTeacher()
teacher1.set_id(5)
teacher1.set_firstname('hooman')
teacher1.set_lastname('javanbakht')
teacher1.set_time(30)
teacher1.set_payment(100_000)
teacher1.set_calpayment()
# print(teacher1)

# ---------------------------------------------

class Animal:

    super_class_attr = {'one': 1, 'two': 2}

    def __init__(self, parm1, parm2):
        self.super_instance_atrr_parm1 = parm1
        self.super_instance_atrr_parm2 = parm2


    def breath(self):
        return 'brethingggg'

    def walk(self):
        return 'walking'

class Dog(Animal):

    dog_class_attr = {'three': 3, 'four': 4}

    def __init__(self, parm1, parm2, parm3):
        super().__init__(parm1, parm2)
        self.dog_instance_attr_parm3 = parm3

    @classmethod
    def sub_class_method(cls):
        print(cls.super_class_attr)

    def running(self):
        return 'running'


class Bird(Animal):

    def fly(self):
        return 'flying'

class Fish(Animal):

    def breath(self):
        return 'fishing breath'


# dog = Dog(1, 2, 3)
# print(dog.walk())
# print(dog.running())
#
# bird = Bird(1, 2)
# print(bird.breath())
#
# fish = Fish(1, 2)
# print(fish.breath())


class A:
    pass

class B:
    pass

class C:
    pass

class SubClass(A, B, C):
    pass

# -----------------------------------------

try:
    age = int(input('enter your age: '))
    print(age + 10)
except ValueError as ex:
    print('something wrong')
    print(ex)


