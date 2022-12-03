import math
N, K = map(int, input().split())
factors=[]
for i in range(1,int(math.sqrt(N)+1)):
  if (N%i)==0:
    factors.append(i)
    factors.append(int(N/i))
factors.sort()
print(factors)
if K<len(factors):
  print(factors[-K])
else:
  print(factors[0])