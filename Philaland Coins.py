t=int(input())
n=[]
for i in range(1,t+1):
  n.append(int(input()))
for j in range(len(n)):
  count=0
  while(n[j]>0):
    n[j]=int(n[j]/2)
    count=count+1
  print (count)