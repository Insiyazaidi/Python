# def printing(name , age):
#     print(f"hello from {name} and age is {age}")



# printing( age = 23  ,name =  "Insiya " ) # keywork argument 

# def sum (a,b=45): 
#     print(a+b)

# sum(2 ) 

def check (st):
    rev=""
    for i in range(len(st)-1 , -1 , -1):
     rev+=st[i]
    if rev==st:
     print("yes")
    else:
       print("no")
   
     
check(input("enter string"))