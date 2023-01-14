list1=[]
for i in range(0,5):
     list1.append(int (input ("Enter a number")))
list2=list1.copy()
print ("Before swapping",list1)
for i in range (0,len(list1)-1,2):
     list1[i]=list2[i+1]
for i in range (1,len(list1),2):
     list1[i]=list2[i-1]     
print ("after swapping",list1)

