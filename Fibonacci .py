
# Dispaly fibonicci series upto a term
n=int(input("Enter number"))
a = 0
b = 1
     
# Check is n is less
# than 0
if n < 0:
    print("Incorrect input")
# Check is n is equal to 0
elif n == 0:
    print ( 0)
       
# Check if n is equal to 1
elif n == 1:
    print( b)
else:
    print (a)
    print (b)
    for i in range(0, n):
        c = a + b
        a = b
        b = c
        print(b)
