# class Factory():
    
#     a = "attribute inside factory , parent class "
#     def __init__(self , name , age):  # this is consturctor 
#         self.name = name   # ADD THIS
#         self.age = age 
#         print(f"{name} , {age}")


#     def hello(self): 
#         print("hello from factory , parent class ")

# class Pune(Factory):  # child class 
#     def __init__(self , name , age , location):
#         super().__init__(name , age)  # from parent class 
#         self.location = location  # child class only 

#     def hello(self):
#         print(f"hello from child {self.name} , {self.age} , {self.location}")


# obj = Factory("insiya" ,23)
# print(obj.a)
# obj.hello()

# obj2 = Pune("zoya" , 1 , "krishna nagar")  # it can access hello from parent 
# obj2.hello()


# If child has its own __init__() and you also want the parent's __init__() to run → use super().__init__().


#MULTIPLE INHERTANCE 

# class Camera:
#     def __init__(self , megapixel , **kwargs):  # kwargs is extra argu just
#         self.megapixel= megapixel
#         print("hello from camera")
#         super().__init__(**kwargs)  # now move to next const 

#     def camprint(self):
#         print(f"{self.megafixel}")

# class Phone():
#     def __init__(self ,  phoneno , **kwargs):
#         self.phoneno = phoneno
#         print("hello from phone")
#         super().__init__(**kwargs)

#     def phoneprint(self):
#         print(f"{self.phoneno}")

# class mydetial(   Phone ,  Camera ):  # this seq matter .. phle Phone ka const call hoga then Camera 
#     def __init__(self , megapixel , phoneno , name):
#          # SIMPLE CALLING EACH CONSTRUCTOR ONE BY ONE 
#      self.name = name
#      super().__init__(
#          # here seq does not matter 
#             megapixel=megapixel ,
#               phoneno=phoneno

#     )
#         #  Camera.__init__(self, megapixel)    # phle camera ka cons call horha h
#         #  Phone.__init__(self, phoneno)        # uske baad phone ka cons call horha h 

#     print("hello from mydetail ")
         
#     def myprint(self):
#       print(f"{self.phoneno} , {self.megapixel} , {self.name}")


# myobj = mydetial("34px" , 741466 , "insiya")

# myobj.myprint()


#multi level  inhertance 

class Factory():
   def __init__(self , material , zip):
      self.material = material
      self.zip  = zip

class Bhopalfac(Factory):
   def __init__(self , material , zip , colour):
      super().__init__(material , zip)
      self.colour = colour

class Punefac(Bhopalfac):
   def __init__(self, material, zip, colour , price):
      super().__init__(material, zip, colour)
      self.price = price

obj = Punefac("leather" , 3 , "blue" , 978)

# hiercial inheritance - one parent , 2 child


