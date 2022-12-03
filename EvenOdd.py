from itertools import product

L, H = map(int, input().split())
K = int(input())
count = 0
li = [i for i in range(L,H+1)]
perm = list(map(list, product(li,repeat=K)))
print(perm)
for i in perm:
    if sum(i)%2==0:
        count += 1
print(count%1000000007)
