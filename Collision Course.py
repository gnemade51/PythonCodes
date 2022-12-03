import math
c=int(input())
l=[]
ans=[]
count=0
for i in range(c):
    x,y,v=input().split()
    x=int(x)
    y = int(y)
    v = int(v)
    d = int((math.sqrt(x*x+y*y))/v)
    l.append(d)
dict = {i:l.count(i) for i in l}
for number in dict.values():
    for i in range(number):
        count+=i
print(count)

"""
5
5 12 1
16 63 5
-10 24 2
7 24 2
-24 7 2
"""