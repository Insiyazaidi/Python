# a = range(1 , 21 , 1)
#for i in a:
    #print(i)

#for i in range(1 , 21 , 1):
    #print(i)

#for i in range(21):  # by default it will start from 0 and step size will be 1 however it is necessary to give ending point 
   # print(i)

# if we want to reverse 

#for i in range(16 , 0 , -1): # it will print from 16 to 1 
   # print(i)

#for i in range(-5 , 3 , 1):
  #  print(i)

#for i in range(5 , 51 , 5):
  #  print(i)
 
#n = int(input("enter the table"))

#for i in range(n , (n*10)+1 , n):
   # print(i)

#a = "INSIYAZAIDI hello from my side"
#for i in range(0 , len(a)  ,1):
  #  print(a[i])

#for i in a :
   # print(i)

#for i in range(1 , 21 ,1):
   # if i==15:
     #   print("break is executed ")
     #   break


  #  print(i)  # if ke bahar, but for loop ke andar
  

#else:
   # print("break not executed ")

#n = int(input("enter number"))
#for i in range(n , 0 , -1 ):
  #  print(i)

    # sum upto n terms
#sum=0

#for i in range(1 , n+1 ):
   # sum+=i

#print(sum)  # agr sum+=i ke saath indent kroge toh yeh within loop consider hoga .. abhi toh bhr h 


#for i in range(1 ,11):
   # print(f"{n} * {i} = {n*i}")

#prod = 1
#for i in range(n , 1 , -1):
   # prod *= i

#print(prod)

# for eg no is 13 

# factors except no itself have sum equal to numb 

# prime no 
#for i in range(2 , n ):
  #  if n%i==0:
     # print("no it is not a prime no ")
   #   break
 #else:  # yeh for - else h ab kyu ki indenation for ke saath  h 
  #      print(" yes no is prime")

#a = "INSIYA"
#b =  " ZAIDI "
#c = ""
#for i in range(len(a)-1 , -1 , -1):
 #c+=a[i]

#print(c+b) # bhr h for loop ke ... kyu ki yeh c+=a ke saath align ni h 

a= "fsfi788754095-40iue"
char= 0
dig=0
spec=0
for i in range(0 , len(a) , 1):
   if a[i].isdigit():
      dig+=1
   elif a[i].isalpha():
      char+=1
   else:
      spec+=1

print(f"your digits are {dig} , char are {char} , special char are {spec}")




