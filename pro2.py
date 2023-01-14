'''
 Write a program to input the value of x and n and print the sum of the following series:
 
o x - x2/2 + x3/3 - x4/4 + ............xn/n
'''
x=int(input ("Enter a number"))
n=int(input ("Enter a number"))
sol=0
for i in range (1,n+1):
     if (i%2==0):
          sol-=(x**i)/i
     else:
          sol+=(x**i)/i
print(sol)
