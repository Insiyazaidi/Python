# p= open(r'func.py')  # yeh same folder m h isliye just file name daal diya h 
# print(p.read())


# q = open(r"C:\Users\LENOVO\Documents\10 June.txt" ,'r')  # provide actual path by default read mode is there 
# print(q.read())

#e = open('superman.txt' , 'w')  # this will create a file or if file is already present  all content will be removed from prev file 
#e = open('superman.txt' , 'a')  # this can create and append the new text and keep prev text also
#e.write("heeelllo insiya adding  ")  # and for this we will write whatveer we want

e= open('nobita.txt' , 'x') # this will onlyy create a file and if file already exist it will give error

e.close()  # to close the file 