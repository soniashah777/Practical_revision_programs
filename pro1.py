'''
Write a program to input the value of x and n and print the sum of the following series:
1+x+x2+x3+x4+. ..........xn'''

x=int(input ("Enter a number"))
n=int(input ("Enter a number"))
sol=1
for i in range (1,n+1):
     sol+=x**i
print(sol)
