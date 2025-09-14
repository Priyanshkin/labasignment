number=int((input("enter a number")))#prime or coprime prime===1,2,3,5,7,,9
count=0
for j in range(1,number+1):
    if number%j==0:
     count=count+1
if count<=2:
 print("prime number")                                 
     #print("your number is even")
elif count>=2: 
     print("number is co-prime")
for j in range(1,11):
    if j==11:
       break
else:
   print("this is not number in range")
