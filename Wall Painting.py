i = int(input())
e = int(input())
i_arr = []
e_arr = []
while i != 0:
    i_arr.append(float(input()))
    i-=1
while e != 0:
    e_arr.append(float(input()))
    e -= 1
cost = 0
for i_wall in i_arr:
    cost += (i_wall*18)
for e_wall in e_arr:
    cost += (e_wall*12)
print("Total estimated Cost : ",cost," INR")