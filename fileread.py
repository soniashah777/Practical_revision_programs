'''
Write a Python Program to read a text file
and display each word separated by #. 
'''
fileobj= open("my.txt","r+")
x=fileobj.read().replace(" ","#")
print (x)
fileobj.close()
