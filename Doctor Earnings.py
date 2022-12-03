li=[]
earn=0
for i in range(20):
    temp = input()
    if temp=='':
        break
    elif int(temp)<=0 or int(temp)>120:
        pass
    else:
        temp = int(temp)
        li.append(temp)
for item in li:
    if item<17:
        earn+=200
    elif item in range(17,41):
        earn+=400
    elif item>40:
        earn+=300
print("Total income ",earn," INR")