
class Factory ():
    _a= "pune" # _a just protected show krne ke liye  usecase kuch ni h 
    __salary = 766787

    def _show(self):
        print(f"hello i am  pune factory {Factory.__salary}")  # we can print these private att by using this 

    def __checking():
        print("hello from private method")

class Bhopal(Factory):
   def calling(self):
       print(super()._a)  # super() ki jgha self._a bhi use krskte h 

   def salpr(self):
       print(f"{super().__salary}")


   def printing(self):
       super()._show()


   def check(self):
         super().__checking()
       

obj = Bhopal()
# obj.calling()
# obj.printing()

# obj.salpr()  # there will be error
# obj.check()  # there will be error as they contain private att and method

# even we can access them from fac class also 
#obj2 = Factory()
#obj2.__checking()
#print(obj2.__salary)

obj = Factory()
obj._show()
#print(obj._a)  # se we can access protected variable outside class also .. so in python protected is not useable 