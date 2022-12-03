def awfulCandy(n,m,s):
    arr=[x for x in range(1,n+1)]
    temp = arr[s::m]
    return(temp[0])

t=int(input())
ques=[]
for i in range(t):
    ques.append(list(map(int, input().strip().split())))
for i in range(t):
    print(awfulCandy(ques[i][0],ques[i][1],ques[i][2]))