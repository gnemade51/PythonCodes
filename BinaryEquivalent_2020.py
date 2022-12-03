N = int(input())
arr = list(map(int, input().split()))
arr_dict = dict()
bin_arr = list()
p = max([len(str(bin(num))[2:])for num in arr])
for num in arr:
    bin_num = bin(num)
    z = p-len(str(bin_num)[2:])
    bin_arr.append("0"*z+str(bin_num)[2:])
    bin_l = list("0"*z+str(bin_num)[2:])
    n0, n1 = bin_l.count("0"),bin_l.count("1")
    arr_dict[num] = [n0,n1]
count = 0
if len(arr) == 1:
    sum0, sum1 = arr_dict[arr[0]][0],arr_dict[arr[0]][1]
    if sum0==sum1:
        count = 1
else:
    for i in range(len(arr)):
        sum0, sum1 = arr_dict[arr[i]][0],arr_dict[arr[i]][1]
        if sum0==sum1:
            count+=1
        for j in range(i+1,len(arr)):
            sum0+=arr_dict[arr[j]][0]
            sum1 += arr_dict[arr[j]][1]
            if sum0 == sum1:
                count+=1
q = len(str(bin(count))[2:])
z = p-q
ans =  "0"*z+str(bin(count))[2:]
print(ans)
