class Car:
    # class attr
    wheel = 4
    engine = 1

    # instance attribute
    def __init__(self, color='black', name='pride'):
        self.color = color
        self.name = name

    # instance method
    def get_color(self):
        return self.color

    #class method
    @classmethod
    def get_wheel(cls):
        return cls.wheel

    # static method
    @staticmethod
    def driving():
        return 'DRIVING...............'


car1 = Car(color='red', name='benz')
car2 = Car(color='blue', name='bmw')
car3 = Car()

# print(car1.wheel)
# print(car2.engine)
# print(car1.get_color())
# print(car2.get_color())
# print(car1.get_wheel())
# print(car2.driving())
# ----------------------------------------


class Calculator:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def multi(self):
        return self.num1 * self.num2

    def divide(self):
        return self.num1 / self.num2


calculator = Calculator(4, 6)

# print(calculator.add())
# print(calculator.multi())
# print(calculator.divide())


class Employee:
    emp_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.emp_count += 1

    def get_count(self):
        return f'total employee is {Employee.emp_count}'

    def get_employee(self):
        return f'name is {self.name} and salary is {self.salary}'

# employee1 = Employee(name='alex', salary=20000)

# print(employee1.name)
# print(employee1.emp_count)
# print(employee1.get_count())

# employee2 = Employee(name='hooman', salary=10000)

# print(employee1.name)
# print(employee1.emp_count)
# print(employee1.get_count())


# -------------------------------------------------------

class Person:
    questions = [
        "I always take the lead in group assignments: ",
        "I always finish my assignments on time: ",
        "Helping others succeed is more important than my own success: ",
        "I work a lot on the side with other things than studies: ",
        "I like to tinker with hardware: "
    ]

    @staticmethod
    def check_result(user_input, message):
        if user_input == 1:
            return message[0]
        elif user_input == 7:
            return message[1]
        else:
            return message[2]

    def check_question_1(self):
        doc_answer = [
            "You never take the lead in group assignments",
            "You always take the lead in group assignments",
            "You sometimes take the lead in group assignments"
        ]
        return Person.check_result(person.answers['1'], message=doc_answer)

    def check_question_2(self):
        doc_answer = [
            "You never finish your assignments on time",
            "You always finish your assignments on time",
            "You sometimes finish your assignments on time"
        ]
        return Person.check_result(person.answers['2'], message=doc_answer)

    def check_question_3(self):
        doc_answer = [
            "Helping others succeed is never more important than your own success",
            "Helping others succeed is always more important than your own success",
            "Helping others succeed is sometimes more important than your own success"
        ]
        return Person.check_result(person.answers['3'], message=doc_answer)

    def check_question_4_and_5(self):
        other_time = person.answers['4'] * 2.5 + person.answers['5'] * 0.75
        if (3.25 <= other_time <= 8.24):
            return "You probably have enough time for your studies"
        elif (8.25 <= other_time <= 13.24): \
            return "You might want to increase time spent on studies"
        else:
            return "You definitely want to increase time spent on studies"

person = Person()
person.answers = {}

print("1 = Not true at all, 7 = Extremely true\n ")
for index, item in enumerate(person.questions, 1):
    user_input = int(input(item))
    person.answers.update({f'{index}': user_input})

print(person.answers)
print(person.check_question_1())
print(person.check_question_2())
print(person.check_question_3())
print(person.check_question_4_and_5())


