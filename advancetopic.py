
# we can import func from diff file/module 

import func


func.check(input("enter string "))

from project import main , extra  # diff folder se multiple files imp krni h toh 

from project.just import handling

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


# def decorate(func):  # hello func is argument for this 
#     def wrapper(*args , **kwargs):
#         print(" the addition to your numb are ")
#         func(*args , **kwargs)
#         print(" thank you ")
#     return wrapper  # this wrapper func will be return 



# @decorate
# def add(a,b):
#     print(f"total is {a-b}")
# add( b =3 ,a=12 ) 


#COMPREHENSIONS 

#LIST
# l= [ i for i in range(1,21) if i%2==0]   # thing u want to add in list , loop , if else cond 

# print(l)

# DICTIONARY
# d ={i : i**2 for i in range(1,10)}  # key , val , loop 
# print(d)

# SETS

# s = {i*i for i in range(1,10) if i%2==0}
# print(s)

#LAMBDA FUNC 

# addition = lambda a: "even" if a%2==0 else "odd" # this is an obj

# print(addition(2))

#MAP 

a = [1 ,2 , 3,4  , 9 , 10]
# def double(x):
#     return x*2
# # result = map(lambda x : x*2 , a)  map need func and storage over which we need to perform operation
# result = map(double , a)  # we can use it withput lambda 
# print(list(result))  # result will be obj se we converted it into list 

# FILTER 


# def even(x):
#     if x%2==0:
#         return True
#     else:
#         return False

# # result=  filter(even, a)

# result=  filter(lambda x: True if x%2==0 else False,  a)

# print(list(result))

