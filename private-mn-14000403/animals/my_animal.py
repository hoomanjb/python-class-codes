class Animal:
    skin = True
    brain = 1
    heart = 1

    def __init__(self, gender, name):
        self.gender = gender
        self.name = name

    def eating(self):
        return 'eating'

    def breath(self):
        pass