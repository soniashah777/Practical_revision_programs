
character =input("enter a string")
count_u_letter=0
count_l_letter=0
count_v_letter=0
count_c_letter=0
for s in character:
    if (ord(s)>=65 and ord(s)<=91):
        count_u_letter+=1
    if (ord(s)>=97 and ord(s)<=123):
        count_l_letter+=1
    if (s=="a" or s=="o" or s=="u" or s=="e" or s=="i"):
        count_v_letter+=1
    else:
        count_c_letter+=1
print("Upper case Letter:",count_u_letter)
print("Lower case Letter:",count_l_letter)
print("Vowels:",count_v_letter)
print("Consonents:",count_c_letter)
