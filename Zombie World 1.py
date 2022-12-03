#penergy = currentenergy +(currentenergy-ZombieEnergy)
t = int(input())
if t in range(1, 11):
  for j in range(t):
    N, T = map(int, input().split())
    if (N in range(1, 51)) and (T in range(1, 101)):
      zomEnergy = list(map(int, input().split()))
      P, D = map(int, input().split())
      if N<=T:
        zomEnergy.sort()
        for i in zomEnergy:
          if P>=i:
            perEnergy = P + (P-i)
            P = perEnergy
        if perEnergy >= D:
          print("YES", end="")
        else:
          print("NO", end="")
      else:
        print("NO", end="")