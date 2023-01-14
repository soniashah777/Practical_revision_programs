'''
Write a Python Program to read a text file
and display each word separated by #. 
'''
fileobj= open("my.txt","r+")
x=fileobj.readlines()
print (len(x))
for i in x:
     print (i)
print (fileobj.closed)
fileobj.close()
