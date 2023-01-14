number=int(input ("Enter a number"))
number_type="None"
for i in range (2,number):
    if(number%i>0):
        number_type="prime"
    else:
        number_type="composite"
        break
print("The number is ",number_type)
