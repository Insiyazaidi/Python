age=int(input("enter the age"))

if age<10:
    print("child")

elif age >10 and age <30 :
    print("adult")
else:
    print("old")

    # century year h toh leap year check krne ke liye 400 se divide kro 
    # century year nhi h toh 4 se divide krke pta lgega 

year = int(input("enter year"))
if year%100==0 and year%400==0:  # all century year is div by 100 
     print("yes its a leap and century year")
elif year%100!=0 and year%4==0:
    print("year it is a leap year but not a century")
else:
    print("neither leap nor century ")
    