def fib(a,b,count):
    fn = []
    for i in range(0, count):
        if i<=1:
            fn.append(i)
        else:
            c=a+b
            fn.append(c)
            a = b
            b = c
    return fn

n1,n2=input().split()
n1=int(n1)
n2=int(n2)
if(n2-n1>=35 and n1,n2>=2 and n1,n2<=100):
    l1=[]
    l2=[]
    l3=[]
    for i in range(n1, n2+1):
        if i > 1:
            if(i==2):
                l1.append(i)
            else:
                for n in range(2, i//2 + 2):
                    if (i % n) == 0:
                        break
                    else:
                        if n == i//2 + 1:
                            l1.append(i)
    for i in l1:
        for j in l1:
            if(i==j):
                pass
            else:
                if j<10:
                    if(((i*10)+j) not in l2):
                        l2.append((i*10)+j)
                elif j>=10:
                    if (((i * 100) + j) not in l2):
                        l2.append((i*100)+j)
    for i in l2:
        if i > 1:
            if (i == 2):
                l3.append(i)
            else:
                for n in range(2, i // 2 + 2):
                    if (i % n) == 0:
                        break
                    else:
                        if n == i // 2 + 1:
                            l3.append(i)
    a=min(l3)
    b=max(l3)
    count=len(l3)
    print(max((fib(a,b,count))))