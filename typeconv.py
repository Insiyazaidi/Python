a = 12 
print(type(a))

a = str(a)
print(type(a))

a = float(a)
print(type(a))

a = bool(a)   # by default cheeze true hogi except->>>  false ,  0 ,  0.0  , "" ,  []  ,  ()  ,  {}  ho toh false 
print(type(a))
print(a)

"""b = "abbdj"  we cant convert a string to int 
b = int(b)
print(type(b))"""

# implicit conv - in this python automatically converts data from one data type to another 
# explicit conv - in this user use inbuild func to  converts data from one data type to another 
d = 12/4
print(d)  # 3.0 not just 3 
print(type(d))