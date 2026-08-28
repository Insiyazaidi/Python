# a=[23 , 43, 67,12 , 0 , "hello" , 'ab' ]

# print(a[3])
# print(a[0:5])

#traversal 

# for i in range(len(a)):  # already excludes the last number 
#     print(a[i])

# for i in a :  # here i will directly conatin elements 
#     print(i)

#METHODS 

# print(dir(list)) , help(list)

# a.append("insiya") # append simply add the val at the last 
# a.append(9)
# a.insert(2 , "zaidi")  # insert take index at which we want to add and the value we want to add 
# a.extend(["faiz" , 72 , 91])  # extend will add things in the list 
# a.remove(9) # remove the first occ of 9 in the list
# index = a.index(67)
# popped_item = a.pop(4) # remove the element at index 4 
# count_72 = a.count(5)  # count the occ of 5 
# # a.sort()
# a.reverse()
# copied_list = a.copy() # create a copy of the list

# print(count_72)
# print(popped_item)
# print(index)
# print(a)
# a.clear()
# print(a)

#l = [12 , 16 , 13 , 19 , 17]

# for i in l:
#     if(i>=0):
#         print(i)

# for i in l:
#     if(i<0):
#         print(i)

# sum = 0
# for i in l:
#     sum+=i
# print(sum//len(l))

# maxel = l[0]
# seclar = 0

# for i in range(1 , len(l)):
#     if(l[i]>maxel):  # this is when we are getting some bigger element 
#         seclar = maxel
#         maxel = l[i]
#     elif l[i]>seclar:  # this cond was missed .. kyu ki chances h ki koi element largest nhi h but vo abhi ke hisb se second largest bn skta h 
#      seclar = l[i]
      
      
# print(maxel , seclar)

#  CHECK IS SORTED
l =[1 , -2, 34 , 7 , 4 , 5 ]

# for i in range(1 , len(l)):
#     if(l[i]<l[i-1]):
#         print("false")
#         break
# else:
#  print("true")
    
# SORTING 
for i in range(0 , len(l)):
    for j in range(i+1 , len(l)):
        if l[j]<l[i]:
         l[i], l[j] = l[j], l[i]
print(l)