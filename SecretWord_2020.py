raw_text = input()
n = int(input())
sec_code = {}
for i in range(n):
    temp1 = {}
    temp2 = {}
    pw, sw = input().split()
    #print(pw)
    #print(sw)
    for i in pw:
        if i in temp1:
            pass
        else:
            temp1[i] = pw.count(i)
    for i in sw:
        if i in temp2:
            pass
        else:
            temp2[i] = sw.count(i)
    for i1,j1 in temp1.items():
        for i2,j2 in temp2.items():
            if j1==j2:
                sec_code[i1] = i2
encoded_word = ""
for char in raw_text:
    encoded_word+=sec_code[char]
print(encoded_word)