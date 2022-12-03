import string
import collections
t = int(input())
for i in range(t):
    N = int(input())
    arr = list(map(int,input().split()))
    monkeys = list(string.ascii_lowercase[:N])
    count = 0
    for j in range(N):
        temp = [0]*N
        temp[arr[j]-1] = monkeys[j]
        count += 1
        if collections.Counter(temp) == collections.Counter(monkeys):
            break
    print(count)