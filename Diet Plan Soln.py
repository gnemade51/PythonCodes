import re
inp1 = re.findall('[0-9]+', input(''))
inp2 = (input('').split('|'))
items = list()
ans = list()
for i in range(0, len(inp2), 1):
    items.append(re.findall('[0-9]+', inp2[i]))
sumP = 0
sumC = 0
sumF = 0
j = 0
while (j<len(inp2)+1 and sumP<=int(inp1[0]) and sumC<=int(inp1[1]) and sumF<=int(inp1[2])):
    for i in items:
        if (sumP+int(i[0])<int(inp1[0]) and sumC+int(i[1])<int(inp1[1]) and sumF+int(i[2])<int(inp1[2])):
            sumP += int(i[0])
            sumC += int(i[1])
            sumF += int(i[2])
        else:
            j += 1
ans.append([(int(inp1[0])-sumP), (int(inp1[1])-sumC), (int(inp1[2])-sumF)])
for i in items:
    if (sumP+int(i[0])<=int(inp1[0]) and sumC+int(i[1])<=int(inp1[1]) and sumF+int(i[2])<=int(inp1[2])):
        sumP += int(i[0])
        sumC += int(i[1])
        sumF += int(i[2])
        g.append([(int(inp1[0])-sumP), (int(inp1[1])-sumC), (int(inp1[2])-sumF)])
        sumP -= int(i[0])
        sumC -= int(i[1])
        sumF -= int(i[2])

ans.sort()
print(ans[0][0], ans[0][1], ans[0][2])
