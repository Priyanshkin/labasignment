string=input("enter a number")
number=int(input("ener a number "))
def hello():
    num=0
    for k in range(0,number):
        num+=1
    return string*num
a=hello()
print(a)
