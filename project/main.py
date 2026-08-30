import os
from pathlib import Path
print("press 1 for creating a file")
print("press 2 for reading a file")
print("press 3 for updating a file")
print("press 4 for deletion a file")

check = int(input("please tell your res"))

def readfileandfolder():
  path = Path('')  # jis folder m hm h uska path aajaiga 
  items = list(path.rglob('*')) # sb ki list aajiagi  , rglob() ka kaam hai folder ke andar files/folders dhundhna * ka matlab yahan roughly:
  for i, item in enumerate(items): # enumerate() 2 cheezein deta hai:
    print(f"{i+1}:{item}")


def createfile():
   try:
      readfileandfolder()
      name = input("tell your file name")
      p = Path(name) # name ko ek Path object mein convert karke p mein store karna
      if not p.exists() and p.is_file():
       with open(p,'w') as fs:  # with ka main fayda hai ki Python kaam khatam hone ke baad file automatically close kar deta hai
        data = input("want you want to write in file")
        fs.write(data)
        print("file created succ")
      else:
       print("file already exist")
   

   except Exception as err:
        print(f"error occ as {err}")



def readfile():
   try:
    readfileandfolder() 
    name = input("which file u want to read")
    p = Path(name)

    if p.exists() and p.is_file():
     with open(p , 'r') as fs:
      data = fs.read()
      print(data)
     print("readed succ ")
    else:
     print("file does not exist")
   except Exception as err:
       print(f"error as {err}")


def updatefile():
   try:
     readfileandfolder()
     filename = input("enter file you want to update")
     p = Path(filename)
     if p.exists and p.is_file():
      print("press 1 for changing name of your file")
      print("press 2 for overwriting data of your file")
      print("press 3 for appending some content in your file")
      print("press 2 for overwriting data of your file")

      res = int(input("tell your response"))
      if res==1:
        name2 = input("tell your new file name")
        p2=Path(name2) 
        p.rename(p2)
      if res ==2:
        with open(p,'w') as fs:
          data = input("enter new data u want to overwrite ")
          fs.write(data)
      if res==3:
         with open(p,'a') as fs:
                  data = input("enter new data u want to append")
                  fs.write(" "+data)
      

   except Exception as err:
    print(f"error is there {err}")



def deletefile():
   try:
    readfileandfolder()
    filename =  input("which file u want to delete ")
    p=Path(filename)
    if p.exists and p.is_file():
      os.remove(p)
      print("file removed succ")
    else:
      print("no such file exist ")
   except Exception as err:
    print(f"error as {err}")
    

if check==1:
   createfile()

if check==2:
   readfile()

if check ==3:
  updatefile()

if check ==4:
  deletefile()


