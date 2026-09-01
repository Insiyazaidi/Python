
import json
import random
import string
from pathlib import Path

class Bank:
   database = 'data.json'
   data =[]

   try:
        if Path(database).exists():  # Path Python ka object banata hai jo file/folder ke path ko represent karta hai.
         with open(database , 'r') as fs: # open() ko file ka naam ya file ka path, dono de sakte ho.
          data = json.loads(fs.read())  
        else:
          print("no such file exist ")
   except Exception as err:
     print(f"an exception occ as {err}")


# json.loads() JSON ko Python object mein convert karta hai, aur json.dumps() Python object ko JSON format mein convert karta hai.

   @staticmethod
   def update():  # iska sirf yhi kaaam h ki dummy data ko data.json file m daal do 
      with open(Bank.database,'w') as fs:
       fs.write(json.dumps(Bank.data))
      



   def createaccount(self):
    info = {
     "name" : input("Tell your name"),
      "age" :int(input("tell your age")),
      "email" : (input("tell your email")),
       "pin" : int(input("tell your pin")),
       "accountNo": 1234,
       "balance":0
}
    if info["age"] <18 or len(str(info["pin"]))!=4:  # pin jo int m tha ab uski len nikalne ke liye string m conv krna padhega 
      print("sorry u cannot create account")
        
    else:
       print("account has been created succ")

       for i in info:
          print(f"{i} : {info[i]}")
          print("Please note down your acc no ")
       Bank.data.append(info)  # info ko data m daaldo 
       Bank.update()  # aur phir is func se data ko database file m daaldo 



user = Bank()  



print("press 1 for creating an account")
print("press 2 for depositing money in the bank")
print("press 3 for withdraw money")
print("press 4 for detail")
print("press 5 for updating the details")
print("press 6 for deleting your account")

check = int(input("tell your response :-  "))

if  check ==1:
   user.createaccount()

