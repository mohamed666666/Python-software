
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self._started = False

    def start(self):
        print("Starting engine...")
        self._started = True

    def stop(self):
        print("Stopping engine...")
        self._started = False




class Car(Vehicle):
    def __init__(self, make, model, year, num_seats):
        super().__init__(make, model, year)# to call the .__init__() method on Vehicle
        self.num_seats = num_seats

    def drive(self):
        print(f'Driving my "{self.make} - {self.model}" on the road')

    def __str__(self):
        return f'"{self.make} - {self.model}" has {self.num_seats} seats'
    



car=Car('Toyota','GTR',1995,4)

print(car)
print(car.year)

car.start()


class Motocycle(Vehicle):
    __wheels=int()
    def __init__(self, make, model, year,wheels):
        super().__init__(make, model, year)
        self.__wheels=wheels
        self.set_wheels(wheels)
    def set_wheels(self,w):
        self.__wheels=w
    def get_wheels(cls):
        return cls.__wheels
    def __str__(self):
        return f'"{self.make} - {self.model}" has {self.num_wheels} wheels'

m=Motocycle('BMW','OfRaod',1995,3)
print(m.get_wheels()) 
print(Motocycle.get_wheels(Motocycle))
m2=m=Motocycle('BMW','OfRaod',1995,2)
print(m2.get_wheels()) 