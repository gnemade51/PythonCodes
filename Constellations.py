N = int(input())
li = []

for i in range(3):  # A for loop for entries
    li.append(list(input().split()))

for i in range(N-2):
    if li[0][i]=='#' and li[1][i]=='#' and li[2][i]=='#':
        print("#",end="")
        continue
    elif li[0][i]=='.' and li[1][i]=='.' and li[2][i]=='.':
        continue
    elif li[0][i]=='.' and li[0][i+1]=='*' and li[0][i+2]=='.' and li[1][i]=='*' and li[1][i+1]=='*' and li[1][i+2]=='*' and li[2][i]=='*' and li[2][i+1]=='.' and li[2][i+2]=='*':
        print('A',end="")
    elif li[0][i]=='*' and li[0][i+1]=='*' and li[0][i+2]=='*' and li[1][i]=='*' and li[1][i+1]=='*' and li[1][i+2]=='*' and li[2][i]=='*' and li[2][i+1]=='*' and li[2][i+2]=='*':
        print('E',end="")
    elif li[0][i]=='*' and li[0][i+1]=='*' and li[0][i+2]=='*' and li[1][i]=='.' and li[1][i+1]=='*' and li[1][i+2]=='.' and li[2][i]=='*' and li[2][i+1]=='*' and li[2][i+2]=='*':
        print('I',end="")
    elif li[0][i]=='*' and li[0][i+1]=='*' and li[0][i+2]=='*' and li[1][i]=='*' and li[1][i+1]=='.' and li[1][i+2]=='*' and li[2][i]=='*' and li[2][i+1]=='*' and li[2][i+2]=='*':
        print('O',end="")
    elif li[0][i]=='*' and li[0][i+1]=='.' and li[0][i+2]=='*'and li[1][i]=='*' and li[1][i+1]=='.' and li[1][i+2]=='*' and li[2][i]=='*' and li[2][i+1]=='*' and li[2][i+2]=='*':
        print('U',end="")