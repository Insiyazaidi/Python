
import json
import random
import string
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

# __file__ -> main.py ka path
# Path(__file__) -> Path object 
# .resolve -> hota h full path nikalne ke liye 
# .parent ek folder peeche/upper level  , yaani ab yeh bankmanagement pr hoga 



class Bank:
   database = BASE_DIR / 'data.json'   # C:\Users\LENOVO\Desktop\Python\project\Bankmanagement\data.json - proper path hi define krdia ,
   # bankmanagemt ke aage data.json lgadia 
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
   def __update():  # iska sirf yhi kaaam h ki dummy data ko data.json file m daal do 
      with open(Bank.database,'w') as fs:
       fs.write(json.dumps(Bank.data))
      

   @classmethod
   def __accountgenerate(cls):
     alpha = random.choices(string.ascii_letters , k=3)
     num = random.choices(string.digits , k=3)
     spchar = random.choices("!@$%^&*" , k=1)
     id = alpha+num+spchar
     random.shuffle(id) # id = ['c', 'a', 'd', 'b'] after shuffle 
     return "".join(id)   # "cabd" create string from list



   def createaccount(self):
    info = {
     "name" : input("Tell your name"),
      "age" :int(input("tell your age")),
      "email" : (input("tell your email")),
       "pin" : int(input("tell your pin")),
       "accountNo": Bank.__accountgenerate(),
       "balance":0
}
    if info["age"] <18 or len(str(info["pin"]))!=4:  # pin jo int m tha ab uski len nikalne ke liye string m conv krna padhega 
      print("sorry u cannot create account")
        
    else:
       print("account has been created succ")

       for i in info:  # info is dic and i will be key 
          print(f"{i} : {info[i]}")
       print("Please note down your acc no ")
       Bank.data.append(info)  # info ko data m daaldo 
       Bank.__update()  # aur phir is func se data ko database file m daaldo 

   def depositmoney(self):

    accnumb =   input("please tell your account numb")
    pin =   int(input("please tell your pin "))
    # find acc no and pin in dummydata 
    # print(Bank.data)

    curruser = [ i for i in Bank.data if i["accountNo"] == accnumb and i["pin"] == pin]  # i will represent dic in each iteration 
     # jo i match krrha h usko list m daaldo 
    # curruser will be a list having a dic 

    # curruser m jo dic h aur Bank.data m jo dic h vo same reference pr h .. yaani ab hm curruser m uupdate krege tohh vo bankdata m bhi change hoga 
    if curruser == False:
       print("Sorry no data found")
    else:
      amount = int(input("enter amount u want to deposit"))
      if amount >10000 or amount < 0:
        print("sorry u cannot deposit this amount")
      else:
        print(curruser)
        curruser[0]['balance']+=amount  # curruser list h usmai dic hai toh curruser[0]-> first element in list which will be dic 
        Bank.__update()   # bank data m update hogya h ... ab json file m krna  h  
 


def withdrawmoney(self):

    accnumb =   input("please tell your account numb")
    pin =   int(input("please tell your pin "))
    # find acc no and pin in dummydata 
    # print(Bank.data)

    curruser = [ i for i in Bank.data if i["accountNo"] == accnumb and i["pin"] == pin]  # i will represent dic in each iteration 
     # jo i match krrha h usko list m daaldo 
    # curruser will be a list having a dic 

    # curruser m jo dic h aur Bank.data m jo dic h vo same reference pr h .. yaani ab hm curruser m uupdate krege tohh vo bankdata m bhi change hoga 
    if curruser == False:
       print("Sorry no data found")
    else:
      amount = int(input("enter amount u want to withdraw"))
      if curruser[0]["balance"]<amount:
        print("sorry u dont have that much money  ")
      else:
        print(curruser)
        curruser[0]['balance']-=amount  # curruser list h usmai dic hai toh curruser[0]-> first element in list which will be dic 
        Bank.__update()   # bank data m update hogya h ... ab json file m krna  h  
 





user = Bank()  



print("press 1 for creating an account")
print("press 2 for depositing money in the bank")
print("press 3 for withdraw money")
print("press 4 for detail")
print("press 5 for updating the details")
print("press 6 for deleting your account")

check = int(input("tell your response :-  "))

if  check==1:
   user.createaccount()

if check==2:
  user.depositmoney()
if check==3:
  user.withdrawmoney()

