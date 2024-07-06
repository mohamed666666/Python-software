"""
Lightweight Classes With .__slots__
.__slots__ attribute can help you reduce the memory footprint of the corresponding instances.
 This attribute prevents the automatic creation of an instance .__dict__. Using .__slots__ is 
 particularly handy when you have a class with a fixed set of attributes, 
 and you’ll use that class to create a large number of objects.
"""

class point:
    __slots__=('x','y')#This attribute prevents the automatic creation of an instance .__dict__. 

    def __init__(self , x ,y) :
        self.x=x
        self.y=y
    '''@property    
    def x(self):   ValueError: 'x' in __slots__ conflicts with class variable
        return self.x'''


p=point(5,6)

print(p.x)
print(p.__slots__)

from pympler import asizeof
print(asizeof.asizeof(p))#ckeck memory effeciency 

#The .__slots__ attribute adds a second interesting behavior to your custom classes. 
#It prevents you from adding new instance attributes dynamically

#p.z=7 #AttributeError: 'point' object has no attribute 'z'
#print(p.z )

p.y=5

print(p.y)


# classes methods and instance methods and static methods 

class Person:
    def __init__(self,name=None,phone=None):# instance method With self
        self.name=name
        self.phone=phone


class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.started = False
        self.speed = 0
        self.max_speed = 200

    # ...
    def start(self):#instance method 
        if not self.started:
            self.started=True

    def stop(self):
        if self.started:
            self.started=False

    def accelerate(self, value):
        if not self.started:
            print("Car is not started!")
            return
        if self.speed + value <= self.max_speed:
            self.speed += value
        else:
            self.speed = self.max_speed
        print(f"Accelerating to {self.speed} km/h...")

    def brake(self, value):
        if self.speed - value >= 0:
            self.speed -= value
        else:
            self.speed = 0
        print(f"Braking to {self.speed} km/h...")

        def __repr__(self):
            return (
            f"{type(self).__name__}"
            f'(make="{self.make}", '
            f'model="{self.model}", '
            f"year={self.year}, "
            f'color="{self.color}")'
        )
        

Toyota=Car("Toyota","Camery",2000,'Wight')

print(repr(Toyota))
a=repr(Toyota)
print(a)



## class methods 
class ThreeDPoint:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __iter__(self):
        yield from (self.x, self.y, self.z)

    @classmethod
    def from_sequence(cls, sequence):
        """In the .from_sequence() class method, you take a sequence of coordinates as an argument, 
        create a ThreeDPoint object from it, and return the object to the caller.
        To create the new object, you use the cls argument,
        which holds an implicit reference to the current class,
        which Python injects into your method automatically.
        """

        return cls(*sequence)

    @staticmethod
    def show_intro_message(name):
        print(f"Hey {name}! This is your 3D Point!")

    def __repr__(self):
        return f"{type(self).__name__}({self.x}, {self.y}, {self.z})"
    


# Encabsulation 


class Bird:
    def __init__(self, name):
        self.set_name(name)

    def get_name(self):
        return self.__name

    def set_name(self, value):
        self.__name = value  #the _name attr is protected attr now so you encabsulate 

b=Bird('FINIK')

print(b.get_name())