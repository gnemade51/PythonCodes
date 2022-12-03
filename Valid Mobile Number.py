li = []
count = 0
while(1):
    temp = input()
    if temp=="Q"or temp=="q":
        break
    else:
        li.append(temp)
if len(li)<5 or len(li)>5:
    print("INPUT LIMIT is 5")
else:
    for item in li:
        if len(item)<=10:
            if item.isdigit() == False:
                count += 1
        else:
            count+=1
    print(count)
