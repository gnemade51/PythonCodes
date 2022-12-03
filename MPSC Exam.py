arr = []
avg = [0]*3
for i in range(3):
    temp = []
    for j in range(3):
        temp.append(int(input()))
        if temp[j]<1 or temp[j]>100:
            temp[j] = 0
    arr.append(temp)
for i in range(3):
    for j in range(3):
        avg[i] += arr[j][i]
    avg[i] //= 3
for i in range(3):
    if avg[i] < 70:
        print("Trainee is unfit")
    if avg[i]== max(avg):
        print("Trainee Number : ", i+1)