v = 65
print(chr(v)) # chr converts unicode to char  

s = "A"
print(ord(s))  # ord converts char to unicode 


# string indexing

a= 'INSIYA ZAIDI'
print(a[3])
print(a[-1])
print(a[6])  # AT 6 IT IS GIVING SPACE MEANS SPACE IS ALSO CONSIDERED WHILE INDEXING 
print(a[7])

# slicing 
# start , stop+1 , step - syntax 
q ="INSIYA ZAIDI"
print(a[0:6:1])
print(a[7:]) # we can even remove the step size val and stop value 
