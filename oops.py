
# class Factory():
#     a=12
#     def hello(self):
#         print("hello")
# print("I am getting initialized ") 

# # print(Factory().a)
# # Factory().hello()

# createdobj = Factory()
# print(type(createdobj))
# print(createdobj.a)
# createdobj.hello()

# class Factory():
#     def __init__(self , brand , seats,  colour):
#         # self ref to the curr  obj 
#         print(self)
#         self.brand = brand
#         self.seats = seats
#         self.colour = colour
#     def show(self):
#         print(f"details are {self.brand} , {self.seats} , {self.colour}")


# toy = Factory("toyota" , 4 , "white")

# bul= Factory("bularo" , 2 , "blue")

# toy.show()
# bul.show()
        

class Animal():
    name = "lion"  # class attribute 
    def __init__(self , colour):
       self.colour = colour  # instance attribute

    def show(self): #instance method
        print(f"hellooo {self.colour} ")

    @classmethod
    def newm(cls): # refers to the class itself ,  cls se class ke variables/methods access kar sakte ho.
        print(f"from new methodd {cls} , {cls.name}")

    @staticmethod # does not target class or object 
    def stm():
        print("from static method")


obj = Animal(12)
obj.show()
obj.newm()
obj.stm()