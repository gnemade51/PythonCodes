def count(arr, l, r):
    c = 0
    # traverse in the list1
    for i in arr:
        # condition check
        if i >= l and i <= r:
            c += 1
    return c

S, R = map(int, input().split()) #samples and ranges
arr = list(map(int, input().split()))
#print(arr)
r = []
for i in range(R):
  r1 = list(map(int, input().split()))
  r.append(r1)
#print(r)
arr.sort()
for j in range(len(r)):
    print(count(arr, r[j][0], r[j][1]), end=" ")