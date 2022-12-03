def faultyKeyboard(i,S):
    if S not in i:
        return 0
    if S in i:
        times = i.count(S)
        return times
    D[i] = moves

    return moves


if __name__ == "__main__":
    D = {}
    T = list(input().split())
    S = input()
    ans = 0
    for i in T:
        ans += faultyKeyboard(i, S)
    print(ans)