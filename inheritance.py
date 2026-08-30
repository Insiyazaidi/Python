class Factory():
    a = "attribute inside factory , parent class "
    def hello(self): 
        print("hello from factory , parent class ")

class Pune(Factory):  # child class 
    pass 

obj = Factory()
print(obj.a)
obj.hello()