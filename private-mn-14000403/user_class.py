from animals.my_animal import Animal

class SeaAnimal(Animal):

    def __init__(self, age, gender, name):
        super().__init__(gender, name)
        self.age = age

    def show_name(self):
        return self.name

    def breath(self):
        return 'sea breathing'

class ZaminiAnimal(Animal):
    def breath(self):
        return 'zamini breathing'

animal = Animal(gender='male', name='lion')
sea_animal = SeaAnimal(name=animal.name, gender=animal.gender, age=5)
zamini_animal = ZaminiAnimal(gender='male', name='panter')
print(animal.name)
print(sea_animal.name)
print(zamini_animal.name)
print(isinstance(sea_animal, Animal))