import math
N, K = map(int, input().split())
arr = list(map(int, input().split()))
for i in range(K):
    l = max(arr)
    x = math.floor(l/2)
    pos = arr.index(l)
    arr[pos] = x
print(sum(arr))