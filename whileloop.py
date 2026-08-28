#numb = int(input("enter the number"))
#revno = 0
#while numb!=0:
 #   lastdig = numb%10
   # revno+=str(lastdig)
 #   revno = revno*10+lastdig
  #  numb=numb//10  #  double slash isliye kyu ki python m / gives float number  
#print(revno)


# guess random number 
import random

rannumb = random.randint(1, 10)
guess = int(input("guess a number"))
trial =1
if guess==rannumb:
    print("ohh you predicted right")
while(guess!=rannumb):
    if guess>rannumb:
        print("go little lower")

    elif guess<rannumb:
        print("go little higher")
        
    guess=int(input("wrong guess think again "))
    trial+=1
print( f"no of trials are {trial}")
