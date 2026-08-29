#a = {3 , 4 ,8 , 9 , 4 , 7 , 8 , "hello" }  # set
  # only unique value will be printed 

# MUTABLE , CAN NOT HAVE DUPLICATES , UNORDERED - CANNOT ACCESS VALUE USING IDX , HETEROGENEOUS - CAN STORE MULTIPLE TYPE BUT NOT EVERYTHING 

# each valuue in set is hashed using a hash func 
# we can only hash string , tuple , number which are immutable 
# ordered like list , disctionries are not allowed 
# b = hash("hello")  # har baar hash ki value alag aati h 
# print(b)

# c = hash((1 , 2 , 866))
# print(c)

# for i in a:
#     print(i)  # this will print in random order depending upon hash value stored in ram 

#METHODS 
# a.remove(9)  # removes 9 - raise error if not found
# a.discard("hii") # removes hii - if not found in set there will be no error 
# print(a)

# a.pop() # in this it randomly pop / remove element in set 
# print (a)
# a.clear()

a = {1 , 2 , 3 , 4 ,5}
b ={4 , 5 , 6 , 7 }
s=a.union(b)  # or we can write a|b
print(s)

intersec = a.intersection(b)  # a&b
print(intersec)

diffa  = a.difference(b)   # a-b  only a no b 
diffb = b.difference(a)   # b-a  only b no a 
print(diffa)
print(diffb)

symdiff = a.symmetric_difference(b)  # same as b.symmetric_difference(a)  this will remove the common elements are give left over 
# we can write it like a^b or b^a 
print(symdiff)



