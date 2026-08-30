# OVERRIDING 

# class Animal():
#     def show(self):
#         print("hello from animal")

# class Human(Animal):
#     def show(self):
#       print("hello from human")

# obj = Human()
# obj.show()   

# OVERLOADING DOES NOT EXSIT IN PYTHON  - AS FUNC WILL BE OVERWRITE 

class Mydetial():
    def hello(self):
        print("hello ")

    def hello(self , name):
       print(f"{name}")

obj = Mydetial()
obj.hello("insiya")
# obj.hello() - will give error as sec func over write first one ,  The second assignment replaces the first one.