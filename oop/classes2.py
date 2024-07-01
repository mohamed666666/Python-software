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

