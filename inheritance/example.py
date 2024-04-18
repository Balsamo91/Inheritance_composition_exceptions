class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name} is eating.")

    def get_age(self):
        print(f"{self.name} is {self.age} years old!")

class Elephant(Animal):
    def trumpet(self):
        print(f"{self.name} makes some noise!")

class Lion(Animal):
    def roar(self):
        print(f"{self.name} roars!")

# Creating instances of Elephant and Lion

elephant = Elephant("Ellie", 10)
lion = Lion("Leo", 5)

elephant.eat()
lion.eat()

elephant.get_age()
lion.get_age()

elephant.trumpet()
lion.roar()

