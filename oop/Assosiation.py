# Composition Has A relation 

class Body:
    def __init__(self):
        self.rotation = 0

    def rotate_left(self, degrees=1):
        self.rotation -= degrees
        print(f"Rotating body {degrees} degrees to the left...")

    def rotate_right(self, degrees=1):
        self.rotation += degrees
        print(f"Rotating body {degrees} degrees to the right...")

class IndustrialRobot:
    def __init__(self):
        self.body = Body()
        self.arm = Arm()

    def rotate_body_left(self, degrees=10):
        self.body.rotate_left(degrees)

    def rotate_body_right(self, degrees=10):
        self.body.rotate_right(degrees)

    def move_arm_up(self, distance=10):
        self.arm.move_up(distance)

    def move_arm_down(self, distance=10):
        self.arm.move_down(distance)

    def weld(self):
        self.arm.weld()



class Arm:
    def __init__(self):
        self.position = 0

    def move_up(self, distance=1):
        self.position += 1
        print(f"Moving arm {distance} cm up...")

    def move_down(self, distance=1):
        self.position -= 1
        print(f"Moving arm {distance} cm down...")

    def weld(self):
        print("Welding...")


r =IndustrialRobot()
r.rotate_body_right(60)
r.rotate_body_left(50)
r.move_arm_up()

print(r.body.rotation)
print(r.arm.position)


#Delegation 
"""
Delegation is another technique that you can use as an alternative to inheritance.
{With delegation, you can model can-do relationships,
where an object hands a task over to another object, }
which takes care of executing the task.
Note that the delegated object can exist independently from the delegator.
"""


class Stack:
    def __init__(self, items=None):
        if items is None:
            self._items = []
        else:
            self._items = list(items)

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def __repr__(self) -> str:
        return f"{type(self).__name__}({self._items})"
#Your Stack class has handed its operations over to the list object, which already knows how to perform them.


print(dir(Stack()))


#CONCLUSION 
"""
With inheritance, the internals of parent classes are visible to subclasses, which breaks encapsulation. 
If some of the parent’s functionality isn’t appropriate for the child, 
then you run the risk of incorrect use.
 In this situation, composition and delegation are safer options.
"""
print("#############")

"""
Finally, in Python, you can quickly implement delegation through the .__getattr__() special method.
 Python calls this method automatically whenever you access an instance attribute or method. 
 You can use this method
 to redirect the request to another object that can provide the appropriate method or attribute.
"""


import json
import pickle

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Serializer:
    def __init__(self, instance):
        self.instance = instance
        print("from serlaizer",instance)

    def to_json(self):
        return json.dumps(self.instance.__dict__)

    def to_pickle(self):
        return pickle.dumps(self.instance.__dict__)

class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def __getattr__(self, attr):#when call instance method this running 
        print("from employee",attr)
        if (attr=='hellow'):
            print("this test form hellow of the emploee eee ")
        return getattr(Serializer(self), attr)


e=Employee('mohmaed',26,12540)
print(e.to_json())#automatically redirected to calling .to_json() on the instance of Serializer. 
print(getattr(Serializer(e),"to_json"))
e.hellow()