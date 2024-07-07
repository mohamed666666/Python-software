

class Aircraft:
    def __init__(self, thrust, lift, max_speed):
        self.thrust = thrust
        self.lift = lift
        self.max_speed = max_speed

    def show_technical_specs(self):
        print(f"Thrust: {self.thrust} kW")
        print(f"Lift: {self.lift} kg")
        print(f"Max speed: {self.max_speed} km/h")

class Helicopter(Aircraft):
    def __init__(self, thrust, lift, max_speed, num_rotors):
        super().__init__(thrust, lift, max_speed)
        self.num_rotors = num_rotors

    def show_technical_specs(self):
        super().show_technical_specs()
        print(f"Number of rotors: {self.num_rotors}")




class Worker:
    def __init__(self, name, address, hourly_salary):
        self.name = name
        self.address = address
        self.hourly_salary = hourly_salary

    def show_profile(self):
        print("== Worker profile ==")
        print(f"Name: {self.name}")
        print(f"Address: {self.address}")
        print(f"Hourly salary: {self.hourly_salary}")

    def calculate_payroll(self, hours=40):
        return self.hourly_salary * hours



class Manager(Worker):
    def __init__(self, name, address, hourly_salary, hourly_bonus):
        super().__init__(name, address, hourly_salary)
        self.hourly_bonus = hourly_bonus

    def calculate_payroll(self, hours=40):
        return (self.hourly_salary + self.hourly_bonus) * hours
    

#MRO dimond problem  Method Resolution Order 



class A:
    def method(self):
        print("A.method")


class C(A):
    def method(self):
        print("C.method")

class B(A):
    def method(self):
        print("B.method")

class D( C,B):
    pass
    """def method(self):
        super().method()"""

print(D.method)

print(D.__mro__)