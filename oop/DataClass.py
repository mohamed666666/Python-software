"""
Python’s data classes specialize in storing data. However, 
they’re also code generators that produce a lot of class-related boilerplate code
 for you behind the scenes.

For example, if you use the data class infrastructure to write a custom class, 
then you won’t have to implement special methods like 
.__init__(), .__repr__(), .__eq__(), and .__hash__(). 
The data class will write them for you. More importantly,
 the data class will write these methods applying best practices and avoiding potential errors.

"""
from enum import Enum # is imuatable dict for necesasry uses 
from dataclasses import dataclass


@dataclass
class Test:
    rank : int | float
    name : str

    @classmethod
    def from_sequence(cls, sequence):
        return cls(*sequence)

t=Test('mohamed',5)

print(Test.from_sequence(['mohamed',14]))#class method 
print(t.from_sequence(['ABCS',18]))
print(t)



class WeekDays(Enum):
    """
    when you want to re assign value of enum element ERROR :
    AttributeError: cannot reassign member 'MONDAY'
    """
    SAT=1
    SUN=2
    MON=3
    TU=4
    WEN=5
    THU=6
    FRI=7

    @classmethod
    def favorite_day(cls):
        return cls.FRI




s=WeekDays(1)
print(s)
print(s.favorite_day().value())

