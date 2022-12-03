def checkPrime(num):
    if num > 1:
        flag = True
        for i in range(2, num):
            if num % i == 0:
                flag = False
        if flag == True:
            return True
        else:
            return False
    return False

D, P = map(int, input().split())
if (D in range(10, 500)) and (P in range(2, 50)) and D%P == 0:
    d = int(D/P)
    li = []
    for i in range(1,d+1):
        temp =[]
        if checkPrime(i):
            temp.append(i)
            for j in range(1,P):
                temp.append(i+(j*d))
            if (checkPrime(temp[1])) and (checkPrime(temp[2])):
                li.append(temp)


print(len(li))
