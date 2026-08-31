
# class Animal:
#     @property
#     def show(self):
#         print("hello")

# obj = Animal()
# obj.show   # using property decorator we can call method without ()

# def decorate(func):  # hello func is argument for this 
#     def wrapper(a,b):
#         print(" the addition to your numb are ")
#         func(a,b)
#         print(" thank you ")
#     return wrapper  # this wrapper func will be return 



# @decorate
# def add(a,b):
#     print(f"total is {a+b}")
# add(12 , 1) 


#ARGS AND KWARGS 
# def addition(*args):   # arg (3 , 4 , 1 , 1) -input  will become tuple 
#     print(args)
#     sum=0
#     for i in args:
#      sum+=i
#     print(sum)

# addition(3 , 4 , 1 , 1)

# def information(**kwargs):   #  dictinory 
#     print(kwargs)
#     for i in kwargs:  # i points to key not on values 
#      print(f"{i} : {kwargs[i]}")

# information(name = "insiya" , age=12 , father = "arhsad")  # kwargs are used for key word arguments


def decorate(func):  # hello func is argument for this 
    def wrapper(*args , **kwargs):
        print(" the addition to your numb are ")
        func(*args , **kwargs)
        print(" thank you ")
    return wrapper  # this wrapper func will be return 



@decorate
def add(a,b):
    print(f"total is {a-b}")
add( b =3 ,a=12 ) 