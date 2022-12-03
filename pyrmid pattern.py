n = int(input())
for i in range(0,n):
    for j in range(0,i+1):
        if j==i:
            print(i+1, end=" ")
        else:
            print(i+1,"*", end=" ")
    print("")
for i in range(n-1,-1,-1):
    for j in range(0,i+1):
        if j==i:
            print(i+1, end=" ")
        else:
            print(i+1,"*", end=" ")
    print("")