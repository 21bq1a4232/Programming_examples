def lru(p,c):
    m=[]
    l=[]
    pg=0
    for i in p:
        if i not in m:
            pg+=1
            if len(m) < c:
                m.append(i)
                l.append(i)
            else:
                d=m.index(l[0])
                m[d]=i
                l.pop(0)
                l.append(i)
        else:
            d=l.index(i)
            l.pop(d)
            l.append(i)
    return pg
pg=[10,20,30,40,50,60,70,80,90,100]
cap=3
print(lru(pg,cap))