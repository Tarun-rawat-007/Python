from abc import ABC,abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class square(Shape):
    def __init__(self,side):
        self.side=side

    def area(self):
        return self.side*self.side

s=square(2)
print(s.area() )
        
