class A:
    _n=0
    __n1=2
    id=10
    def __init__(self,id=None,name=None):
        self.id=id
        self.name=name
        #print(self)  commented when added __Str__ method TypeError: __str__ returned non-string (type NoneType)
        #return self
    def print_private(self):
        print(self.__n1)

    def __str__(self) -> str:
        #print(__name__)
        return self.name
    def edit_static_id(self):
        type(self).id+=10
        print(A.id)

    
    
#Note when update the code the hash of object chages even if add comment or delete comment 

a2=A(1,'mohamed')

a=A()
# the id of instance a 
print(a.id)

# the id of A is static one cause it intialized in the body of the class  
print(A.id)
'''
print(A.name) Gives error cause name is instance attrebuite 
'''
A.edit_static_id(a)
a.edit_static_id()
a2.edit_static_id()

print(a._n)#protected variable _n 
#print(a.__n1) AttributeError: 'A' object has no attribute '__n1'

print(a2.id)
a.print_private()
print(a._A__n1) # the __n1 is class attr 


#print(str(a))  TypeError: __str__ returned non-string (type NoneType)
print(str(a2))

# dict method 

print(A.__dict__)

print(a2.__dict__)
###################################################

#adding attributes 
class record:
    def __init__(self) -> None:
        pass

john = {     "name": "John Doe",
     "position": "Python Developer",
    "department": "Engineering",
     "salary": 80000,
    "hire_date": "2020-01-01",
     "is_manager": False,
 }

john_record = record()

for field, value in john.items():
    setattr(john_record, field, value)

print(john_record.name)


#adding methods 
class user:
    pass



def __init__(self, name, job):
    self.name = name
    self.job = job

u=user()

user.__init__ = __init__

linda=user('linda','developer')

print(linda.__dict__)

##Property and Descriptor-Based Attributes

"""
Python allows you to add function-like behavior on top of existing instance attributes
 and turn them into managed attributes.
 This type of attribute prevents you from introducing breaking changes into your APIs.
"""

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if not isinstance(value, int | float) or value <= 0:
            raise ValueError("positive number expected")
        self._radius = value

    def calculate_area(self):
        return round(math.pi * self._radius**2, 2)

print("##### Propetry ######")

c=Circle(4)
print(c.calculate_area())
c.radius=5#-5 gives value error 
print(c.calculate_area())

