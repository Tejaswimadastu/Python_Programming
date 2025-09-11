from abc import ABC,abstractmethod
import math
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        return self.length * self.breadth
class Circle(Shape):
     def __init__(self,radius):
         self.radius=radius
     def area(self):
          return math.pi*self.radius**2
r=Rectangle(5,15)
c=Circle(8)
print("Rectangle area ",r.area())
print("Circle area ",c.area())