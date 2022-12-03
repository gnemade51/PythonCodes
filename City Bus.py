import math


def fare(s,d):
    path = [800,600,750,900,1400,1200,1100,1500]
    stop = ["TH","GA","IC","HA","TE","LU","NI","CA"]
    res = 0
    add = 0
    if s==d:
        print("INVALID INPUT")
    else:
        s1 = stop.index(s)
        d1 = stop.index(d)
        if s1>d1:
            temp_arr = path[s1+1:]+path[:d1+1]
        else:
            temp_arr = path[s1+1:d1+1]
        add = float(sum(temp_arr))
        res = float(math.ceil(add/200))
        return res

s = input()
d = input()
s = s.upper()
d = d.upper()
print(fare(s,d),"INR")