
name=input("enter a your name")
s=tuple(name.split())
print(s)
b=s[-1::-1]
for j in b:
    print(j,end=' ')
"""
output=enter a your namepriyansh bajpai shukla
('priyansh', 'bajpai', 'shukla')
shukla bajpai priyansh
"""
#slicing concept
value=tuple((input("1enter a number")))
print(value[0:1:1])
""" goal is to find x=
time-1=enter a number 12345XZ
('1',)
time=2:-
"""
print(value[5:7:2])
"""
 goal is to find x
enter a number12345XZ
('X',)
"""
print(value[-1:-4:-2])  
"""
goal is find value 5
nter a number12345XZ
('Z', '5')
"""  
print(value[-3:-4:-1]) 
"""
goal is find value 5
nter a number12345XZ
('5',)

"""
print(value[4:5:1])  
"""
goal is find value 5
nter a number12345XZ
('5',)
"""


  
