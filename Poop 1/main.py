class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = Person("Will", 18)
print(person1.name)
print(person1.age)
person2 = Person("Liem", 14)
print(person2.name)
print(person2.age)

class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

car1 = Car("Ford", "Ford GT", 1998, "Blue")
print(car1.make, car1.model, car1.year, car1.color)

