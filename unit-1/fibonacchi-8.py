#number=int(input("enter a number"))
#o 1 1 2 3 5  8 13 21 34
#i=0,n+i=0,
# #i=1,n+i=1
# i=2 ,n+2=2
# i=3 ,n+i=3     
n=0
a=[0,1]
print(f"{a[0]} ,{a[1]}",end=' ')
for i in range(2,11):
    v1=a[i-1]
    v2=a[i-2]
    v3=v2+v1
    a.insert(i,v3)
    print(f",{a[i]}",end=' ')