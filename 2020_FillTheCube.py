#incomplete


def arrangeMatrix(M):
    for i in M:
        i.sort()
    return M


# Function to rotate a matrix
def rotate90Clockwise(A):
    N = len(A[0])
    for i in range(N // 2):
        for j in range(i, N - i - 1):
            temp = A[i][j]
            A[i][j] = A[N - 1 - j][i]
            A[N - 1 - j][i] = A[N - 1 - i][N - 1 - j]
            A[N - 1 - i][N - 1 - j] = A[j][N - 1 - i]
            A[j][N - 1 - i] = temp

def printMaxSubSquare(M):
    R= len(M)
    C = len(M[0])
    S = [[0 for k in range(C)] for l in range(R)]
    for i in range(1, R):
        for j in range(1, C):
            if (M[i][j] == "D"):
                S[i][j] = min(S[i][j - 1], S[i - 1][j],
                              S[i - 1][j - 1]) + 1
            else:
                S[i][j] = 0
    max_of_s = S[0][0]
    for i in range(R):
        for j in range(C):
            if (max_of_s < S[i][j]):
                max_of_s = S[i][j]
    return max_of_s

# Driver Program
N = int(input())
mat = []
ans = []
for i in range(N):  # A for loop for entries
    mat.append(list(input().split()))
for i in range(4):
    rotate90Clockwise(mat)
    mat = arrangeMatrix(mat)
    #print(mat)
    ans.append(printMaxSubSquare(mat))

print(max(ans))
