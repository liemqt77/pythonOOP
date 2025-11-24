class Car:
    def __init__(self, make, model, year, engine):
        self.make = make
        self.model = model
        self.year = year
        self.engine = engine

    def gaspedal(self):
        print("f {self.make} is run" )

class Ford:
    pass

class BMW:
    pass

class Toyota:
    pass

ford = Ford("Ford")