class Person:
    def __init__(self, name, age, hobbies):
        self.name = name
        self.age = age
        self.hobbies = hobbies

person1 = Person("Will", 20, "Football")
print(person1.name)
print(person1.age)
print(person1.hobbies)


person2 = Person("Liem", 14, "Basketball")
print(person2.name)
print(person2.age)
print(person2.hobbies)


person3 = Person("Akira", 20, "Boxing")
print(person3.name)
print(person3.age)
print(person3.hobbies)

class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

car1 = Car("Ford", "Ford GT", 1998, "Blue")
print(car1.make, car1.model, car1.year, car1.color)

