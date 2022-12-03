#incomplete
#20F 30C 40P
import itertools
def inpsort(inp):
    res = [0, 0, 0]
    for i in inp:
        if i[-1] == 'P':
            res[0] = int(i[:-1])
        elif i[-1] == 'C':
            res[1] = int(i[:-1])
        elif i[-1] == 'F':
            res[2] = int(i[:-1])
    return res


inp1 = list(map(str, input().split()))
req = inpsort(inp1)

#print(req)
inp2 = list(map(str, input().split("|")))
item = []
for i in range(len(inp2)):
    item.append(inpsort(inp2[i].split()))

count = [0]*len(item)
tempP = tempC = tempF = 0
for j in itertools.count(start=1):
    for i in range(len(item)):
        if (tempP + item[i][0]) >= req[0] or (tempC + item[i][1]) >= req[1] or (tempF + item[i][2]) >= req[2]:
            print(req[0] - tempP, " ", req[1] - tempC, " ", req[2] - tempF)
            break
        else:
            tempP += item[i][0]
            tempC += item[i][1]
            tempF += item[i][2]