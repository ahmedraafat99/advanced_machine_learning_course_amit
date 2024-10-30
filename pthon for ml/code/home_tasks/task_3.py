from abc import ABC, abstractmethod


class animal(ABC):
    @abstractmethod
    def sound(self):
        pass

    def describe(self):
        print("This is a animal.")


class dog(animal):
    def sound(self):
        return "i am dog"

class cat(animal):
    def sound(self):
        return "i am cat"

class cow(animal):
    def sound(self):
        return "i am cow"


animals = [dog(), cat(), cow()]
for animal in animals:
    animal.describe()
    print(animal.sound())