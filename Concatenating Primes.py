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


n = int(input())
if n <= 70:
    l1 = []
    l2 = []
    for i in range(n):
        if checkPrime(i):
            l1.append(i)
    for i in l1:
        for j in l1:
            temp = int(str(i) + str(j))
            if checkPrime(temp):
                if(temp not in l2):
                    l2.append(int(str(i) + str(j)))
    print(len(l2))