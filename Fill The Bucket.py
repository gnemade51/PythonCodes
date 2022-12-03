b = int(input())
m = int(input())
temp = 0
count = 0
if m>b:
    print("INVALID INPUT")
while(temp<((4 / 5) * b)):
    i = int(input())
    if i<0 or i>m:
        print("INVALID INPUT")
        break
    temp+=i
    count+=1
if (temp >= ((4 / 5) * b) and (temp < b)):
    print("BUCKET FULL!")
    print("NUMBER OF MUGS:", count)