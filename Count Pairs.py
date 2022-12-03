
n=list(map(int,input().split())) #integer k is taken as the 2nd number in the list i.e.n[1]=k
#n,k=map(int, input().split())
arr=list(map(int,input().split()))

count=0

for i in range (len(arr)):
    min=arr[i]-n[1] #upper limit of range
    max=arr[i]+n[1] #lower limit of range
    happy = 0
    for x in range (len(arr)):
        if not (i==x):
            if(min <= arr[x]<= max):
                happy = 1
    count = count + 1 if(happy == 1) else count + 0
print(count)