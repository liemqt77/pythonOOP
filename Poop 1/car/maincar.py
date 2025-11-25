class Car:
    def __init__(self, make):
        self.make = make


    def gaspedal(self):
        print(f"{self.make} Engine is start" )

class Ford(Car):
    pass

class BMW(Car):
    pass

class Toyota(Car):
    pass

ford = Ford("Viper")

bmw = BMW("M2")

toyota = Toyota("Supra")

print(ford.make)
Car.gaspedal(ford)