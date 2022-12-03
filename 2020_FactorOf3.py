#complete

# from itertools import permutations
#
# def divthree(i):
#     flag = False
#     for j in range(len(i)-1):
#         if (i[j]+i[j+1])%3==0:
#             flag = False
#             break
#         else:
#             flag = True
#             continue
#     return flag
#
# T = int(input())
# for i in range(T):
#     N = int(input())
#     arr = list(map(int, input().split()))
#     perm = list(permutations(arr))
#     perm = list(dict.fromkeys(perm))
#     #print(perm)
#     flag = False
#     for i in perm:
#         if divthree(i)==False:
#             continue
#         else:
#             flag = True
#             break
#     if flag:
#         print("YES")
#     else:
#         print("NO")
# _______________________________________________





T = int(input())
for i in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    zero_0 = 0
    one_1 = 0
    two_2 = 0
    # perm = list(permutations(arr))
    # perm = list(dict.fromkeys(perm))
    for i in arr:
        rem = i%3
        if rem == 0:
            zero_0 += 1
        elif rem == 1:
            one_1 += 1
        else:
            two_2 += 1

    if (zero_0==0 and one_1!=0 and two_2!=0) or (zero_0>(one_1+two_2+1)):
        print("NO")
    else:
        print("YES")