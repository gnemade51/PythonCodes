import math
def dist(x1,x2,y1,y2,z1, z2):
    d = math.sqrt(math.pow(x2 - x1, 2)+math.pow(y2 - y1, 2)+math.pow(z2 - z1, 2) * 1.0)
    return d
def area(side1, side2, side3):
    s = (side1+side2+side3)/2
    area = math.sqrt(s*(s-side1)*(s-side2)*(s-side3))
    return area



H = int(input())#h  10
pos = list(map(int, input().split()))#a,b,c,d 5 5 5 5
vel = list(map(int, input().split()))#v1,v2,v3 1 1 1 1
dir = list(map(str, input().split()))#U U D D
x = [0]*100#
y = [0]*100#
z = [[0]*100]*4#


ab = [0]*100#
bc = [0]*100#
ac = [0]*100#
ad = [0]*100#
bd = [0]*100#
cd = [0]*100#

abc = [0]*100#
adc = [0]*100#
abd = [0]*100#
bcd = [0]*100#

if (dir[0] == 'D'):
    vel[0]=vel[0]*(-1)
if (dir[1] == 'D'):
    vel[1]=vel[1]*(-1)
if (dir[2] == 'D'):
    vel[2]=vel[2]*(-1)
if (dir[3] == 'D'):
    vel[3]=vel[3]*(-1)



x[0], y[0] = 0, H*(-1)
x[1], y[1] = H, H*(-1)
x[2], y[2] = H, 0
x[3], y[3]= 0, 0
z[0][0] = pos[0]
z[0][1] = pos[1]
z[0][2] = pos[2]
z[0][3] = pos[3]
for i in range(1,100):
    z[i][0] = z[i-1][0] + vel[0]
    z[i][1] = z[i-1][1] + vel[1]
    z[i][2] = z[i-1][2] + vel[2]
    z[i][3] = z[i-1][3] + vel[3]
    if z[i][0] > H:
        z[i][0] = H
    if z[i][0] < 0:
        z[i][0] = 0
    if z[i][1] > H:
        z[i][0] = H
    if z[i][1] < 0:
        z[i][1] = 0
    if z[i][2] > H:
        z[i][2] = H
    if z[i][2] < 0:
        z[i][2] = 0
    if z[i][3] > H:
        z[i][3] = H
    if z[i][3] < 0:
        z[i][3] = 0
for i in range(100):
    ab.append(dist(x[0]),x[1],y[0],y[1],z[i][0],z[i][1])
for i in range(100):
    bc.append(dist(x[1]),x[2],y[1],y[2],z[i][1],z[i][2])
for i in range(100):
    ac.append(dist(x[0]),x[2],y[0],y[2],z[i][0],z[i][2])
for i in range(100):
    ad.append(dist(x[0]),x[3],y[0],y[3],z[i][0],z[i][3])
for i in range(100):
    bd.append(dist(x[1]),x[3],y[1],y[3],z[i][1],z[i][3])
for i in range(100):
    cd.append(dist(x[2]),x[3],y[2],y[3],z[i][2],z[i][3])
for i in range(100):
    abc[i] = area(ab[i], bc[i], ac[i])
for i in range(100):
    adc[i]=area(ad[i], cd[i], ac[i])
for i in range(100):
    abd[i] = area(ab[i], ad[i], bd[i])
for i in range(100):
    bcd[i] = area(bc[i], cd[i], bd[i])

maxabc = max(abc)
minabc = min(abc)
maxadc = max(adc)
minadc = min(adc)

ans1 = 4 * math.pow((maxabc + maxadc), 2)
ans2 = 4 * math.pow((minabc + minadc), 2);
print(round(ans1), round(ans2))