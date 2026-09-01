
import json
import random
import string
from pathlib import Path

class Bank:
   database = 'data.json'
   data =[]

   try:
        if Path(database).exists():
         with open(database , 'r') as fs:
          data = json.loads(fs.read())

   except Exception as err:
     print(f"an exception occ as {err}")


def createaccount(self):
  pass



user = Bank()  



print("press 1 for creating an account")
print("press 2 for depositing money in the bank")
print("press 3 for withdraw money")
print("press 4 for detail")
print("press 5 for updating the details")
print("press 6 for deleting your account")

check = int(input("tell your response :-  "))

#if  check ==1:

