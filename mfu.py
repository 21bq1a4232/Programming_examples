from collections import defaultdict
def mfu(p,c):
    m=[]
    f=defaultdict(int)
    pg=0
    for i in p:
        if i not in m:
            pg+=1
            if len(m) < c:
                m.append(i)
                f[i]=1
            else:
                l=max(m,key=lambda p:f[p])
                m.remove(l)
                m.append(i)
                f[i]=1
        else:
            f[i]=1
    return pg
pg=[10,20,30,40,50,60,70,80,90,100]
cap=3
print(lfu(pg,cap))