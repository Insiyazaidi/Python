#d = {10: 100 , 20:"hello" , 8: 49, "insiya":"zaidi"}
# key value pair , key is unique 
# print(d[8])  # we can access value using key 
# print(d["insiya"])

# CRUD OPER

#UPDATE 
# d[10] = 300  # changed value but we cant change key
# print(d)

# # CREATING / ADDING VALUES IN DIC

# d.update({"faiz":"mohd"})  # M1 
# d["kahkashan"] = "arshad"  # M2
# print(d)

# #DELETE
# del d[20]
# print(d)

# TRAVERSE IN DIC
# for i in d:
#     print(i) # this will print all keys no value
#     print(d[i])  # now this will print value


# for i in d.values():  # this will directly iterate over  values 
#     print(i)

# for i in d.keys():  # vaise keys likhne ki zarrorat ni h vo by default for i in d krke i print kroge toh vo keys hi print krega 
#     print(i)

#METHODS 

# d.clear()

# DEEP AND SHALLOW COPY 

# e = d.copy() # this will return a shallow copy that mean any changes in made in e will not be shown in d and vice - versa 
# e[10] = "muslim"
# print(e)
# print(d)

# if we dont use .copy then deep copy will be created and changes get refected 
# e=d
# e[20]="waahh"  # this will be reflected in both e and d 
# print(e)
# print(d)

#print(d.get(8))  # just another way of printing values using key 

# print(d.items())
#print(d.keys())

# val = d.pop("insiya") # this will remove insiya key and return corresponding val 
# print(val)
# print(d) # insiya will be removed 

#IMP
#MERGE TWO DIC 
#d1={10:100 , 20:200,30:300 , 40:900}
# d2={40:400 , 5:699, 6:13 }

# for i in d2:  # i will point to key in d2 
#     d1[i] = d2[i]  # this means d1[key] agr exist krti hogi toh uski value d2[key] m jo h vo daal do aur in case vo present ni h key d1 m toh new key 

#     # bna kr daal do 

#     print(d1)  # 40:400 now in d1 
# sum 
# sum=0 
# for i in d1 :
#   sum+=d1[i]
# print(sum)   

# count freq of each element in a list 
a = [1,1,1,2,3,3,4,4,5,5,6, 7 , 8 , 8 , 5 ]

# dict={1:3 , 2:1 , 3:2 .... } we need to create like this 

d = {}
for i in a : # traversing over list 
  if i in d.keys():  #  d.keys() → dictionary ke sirf keys ,,,    if this i exist as key in dic  
    d[i]+=1  # add +1 to vlue 
  else:
    d[i]=1
  
print(d)