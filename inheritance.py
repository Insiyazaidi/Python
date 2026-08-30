class Factory():
    a = "attribute inside factory , parent class "
    def __init__(self , name , age):  # this is consturctor 
        print(f"{name} , {age}")


    def hello(self): 
        print("hello from factory , parent class ")

class Pune(Factory):  # child class 
    def __init__(self , name , age , location):
        super().__init__(name , age)  # from parent class 
        self.location = location  # child class only 

        print(f"{name} , {age} , {location} from child class")


obj = Factory("insiya" ,23)
print(obj.a)
obj.hello()

obj2 = Pune("zoya" , 1 , "krishna nagar")  # it can access hello from parent 
obj2.hello()
