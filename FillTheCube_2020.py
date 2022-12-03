# import math
#
# def count1(i):
#     return i.count("D")
#
# n = int(input())
# mat = []
# counter = 0
# for i in range(n):
#     mat.append(list(map(str,input().split())))
# for i in mat:
#     counter += count1(i)
# print(math.floor(math.sqrt(counter)))

# def findmin(arr, arr_copy, N):
#     if N==0:
#         return 0
#     for i in range(N):
#         arr[i].sort()
#         arr_copy[i].sort()
#     mw = 0
#     mt = 0
#     for i in range(N):
#         c = arr[i].count('C')
#         mw = max(mw,c)
#         c = arr_copy[i].count('C')
#         mt = max(mt, c)
#     return min(mw, mt)
# N = int(input())
# arr = [[i for i in input().split()[:N]]for j in range(N)]
# arr_copy = [[0 for i in range(N)]for j in range(N)]
# for i in range(N):
#     for j in range(N):
#         arr_copy[j][i] = arr[i][j]
# res = findmin(arr, arr_copy, N)
# print(res, end='')




def maximumCube(arr, arr_copy, N):
    if N == 0:
        return 0
    for i in range(N):
        arr[i].sort()
        arr_copy[i].sort()
    largew = larget = 0
    for i in range(N):
        temp = arr[i].count('C')
        largew = max(largew, temp)
        temp = arr_copy[i].count('C')
        larget = max(larget, temp)
    return min(largew, larget)

N = int(input())
arr = [[i for i in input().split()[:N]] for j in range(N)]
arr_copy = [[0 for i in range(N)] for j in range(N)]
for i in range(N):
    for j in range(N):
        arr_copy[j][i] = arr[i][j]
f = maximumCube(arr, arr_copy, N)
print(f, end='')