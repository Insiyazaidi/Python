# numb = int(input("enter numb"))
# try:
#  print(10/numb) # now if we do 10/0 there will be zero division exception 

# except Exception as err:
#  print(f"sorry there is error as {err}")

# else: # this will execute only when there is no exception 
#  print("good there is no error ")

# finally:
#  print("i will run no matter what ")


# print("now moving further ... ")  # yeh tb bhi chlega jb error hoga 

age = int(input("enter age"))
try:
 if age<10 or age>18:  # khud se hi apni error line generate krrhe h  
   raise ValueError("your age must be btw 10 and 18")
 else:
   print("welcome")

except Exception as err:  # aur phir usko yha handle krrhe h  
  print(f"we got an error as {err}")

print("the club will start soon")
