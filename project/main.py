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
      p = Path(name) # adding in list of files 
      if not p.exists() and p.is_file():
       with open(p,'w') as fs:
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

if check==1:
   createfile()

if check==2:
   readfile()


 


