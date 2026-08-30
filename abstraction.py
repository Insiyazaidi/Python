from abc import ABC , abstractmethod

class abstract(ABC):
    @abstractmethod
    def perimeter(self):
        pass
    @abstractmethod
    def area(self):
            pass


class Square(abstract): # agr abs class inherit krliya toh mandatory h ki perimeter aur area hme pakka define krne hoge child class m 
     def __init__(self , side):
          self.side = side
     def perimeter(self):
          print(" i have created perimeter")
     def area(self):
                print(" i have created area")



class Circle(abstract):
     def __init__(self , radius):
          self.radius = radius
     def perimeter(self):
      print(" i have created perimeter")
     def area(self):
            print(" i have created area")



obj = Circle(3)

obj2 = Square(5)