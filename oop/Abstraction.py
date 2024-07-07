from abc import ABC ,abstractmethod 

#interface shape is the abstract class with no impelmentation of its methods that every class want to implement 

class Shape(ABC):
    @abstractmethod
    def calc_area():
        pass
    @abstractmethod
    def get_perimeter():
        pass

class square(Shape):
#TypeError: Can't instantiate abstract class square without an implementation for abstract method 'get_rad'
    def __init__(self ,side):
        self._side=side
    def calc_area(self):
        return self._side*self._side
    def get_perimeter(self):
        return self._side*4
s=square(5)
print(s.calc_area())
        
print(s.get_perimeter())

print(type(s))
print(dir(s))