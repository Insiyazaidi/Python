class Animal:
    def __init__(self , name , age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"how from this str dender method and name is {self.name}"

    def __add__(self, other): # other will be tuple for one eg 
        sum =0
        for i in other:
            sum+=i.age
        return f"your sum of ages are {self.age + sum }"

obj = Animal("lion" , 12)
obj2  = Animal("dolphin" , 14)
obj3  = Animal("Tiger" , 42)

print(obj+( obj2 , obj3))

# normal koi func hotta toh obj.__str__() aise krke call krna padhta 

# pr dender method m aisa ni hota h
# print(obj) # dender methods krta h ki jb obj ko print krte ho vo __str__ func ko access krleta h aur location bhi chli jaati h obj ki 
