def sstDiskScheduling(l,h):
    sk=0
    while len(l)!=0:
        mt=l[0]
        for j in range(len(l)):
            tsk = abs(l[j]-h)
            if mt-h> tsk:
                mt=l[j]
        sk+=abs(h-mt)
        h=mt
        l.remove(mt)
    return sk
l=[176,79,34,60,92,11,41,114]
h=50
print(sstDiskScheduling(l,h))