m_arr = [x for x in range(1,101)]
inp1 = list(map(int, input().strip().split(",")))
m = inp1[0]
N = inp1[-1]
del inp1[0]
del inp1[-1]
for i in inp1:
    temp1 = m_arr[0::i]
    temp2 = m_arr[1::i]
    m_arr = temp1[::-1] + temp2[::-1]
print(m_arr[N-1])