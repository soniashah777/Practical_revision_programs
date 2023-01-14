'''
Write a Python Program to read a text file
and display each word separated by #. 
'''
with open("my.txt","r+") as fileobj:
     x=fileobj.readlines()
     print (len(x))
     for i in x:
          print (i)
print (fileobj.closed)

