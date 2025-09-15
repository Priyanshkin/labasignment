string=list(input("enter a word"))
print(string)
enter=int(input("enter a number for remove a word from the list"))
string.remove(string[enter])
print(string)
#ways of find length in list
count=0
for j in string:
    count=count+1
print(count)
s=string.__sizeof__()
b=string[0].__sizeof__()
t=s/b
print(t)
print(b)
#finding of element ways in list
for j in string:
    if(j=='k'):
        print("element is exist")
else:
    print("element not exist")        
    #ways of clear a list 
import copy
#deep copy concept 
b=copy.deepcopy(string)
print(b)
b.clear()
print(b) 
print(string)   
print(string[-1::-1])
a=str(string)
print(a)
#sum of list ele=s=empty+iterstor
c=[1,9,0,3,5]
a=c.__len__()
print(a)
sum=0

for j in range(0,a):
    sum=c[j]+sum
print(sum)
#multiplying 
for j in range(0,a):
    sum=c[j]*sum
print(sum)
#
index=c[3]
for j in c:
    if (j<c[index]):
        index=j
print("sallest",index)

index=c[3]
for j in c:
    if (j>index):
        index=j
print("largest",index)
b=[]
index=c[3]
for j in c:
    if (j<c[index]):
        index=j

