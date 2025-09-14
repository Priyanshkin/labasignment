number1=list(input("enter a number"))
print(number1)
count=0
for j in number1:
    k=tuple(j[0])
    for t in k:
     if t==' ':
        continue
     count=count+1
print(count)
"""
#output->enter a number123 123
['1', '2', '3', ' ', '1', '2', '3']
6
"""