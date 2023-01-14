'''
 Write a program to input the value of x and n and print the sum of the following series:
x/2! + x2/2! - x3/3!+ x4/4! ...................................xn/n!
   '''
x=int(input ("Enter a number"))
n=int(input ("Enter a number"))
sol=0
for i in range (1,n+1):
     if (i%2==0):
          factorial=1
          for k in range(1,i + 1):
               factorial = factorial*k
          print ("Factorial=",factorial)
          sol+=(x**i)/factorial
          print ("Sol=",sol)
     else:
          factorial=1
          for k in range(1,i + 1):
               factorial = factorial*k
          print ("Factorial=",factorial)
          sol-=(x**i)/factorial
          print ("Sol=",sol)
print(sol)
