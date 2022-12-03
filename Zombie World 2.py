#perenergy = curreergy - ((Zi%2)+(Zi/2))
B, N = map(int, input().split())
zomEnergy = list(map(int, input().split()))
if(B>=min(zomEnergy)):
  zomEnergy.sort()
  for i in zomEnergy:
    B = B - ((i%2)+int(i/2))
  if B > 0:
    print("YES")
  else:
    print("NO")
else:
  print("NO")