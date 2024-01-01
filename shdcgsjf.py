from matplotlib import pyplot as pt
def scandisk(l,h):
    le=[]
    r=[]
    sk=0
    for i in l:
        if i<=h:
            le.append(i)
        else:
            r.append(i)
    le.sort()
    r.sort()
    for i in range(len(l)-1,-1,-1):
        sk+=abs(h-le[i])
        h=le[i]
    sk+=abs(h-0)
    h=0
    for i in range(len(r)):
        sk+=abs(h-r[i])
        h=r[i]
    x=sorted(le,reverse=True)+[0]+r
    print(sk)
    plt.rcParams['xtick.bottom'] = plt.rcParams['xtick.labelbottom'] = True
    plt.rcParams['xtick.top'] = plt.rcParams['xtick.labeltop'] = True
    y = list()
    for i in range(len(x)):
        y.append(i*3)
    pt.plot(x,y)
    pt.ylim(0,len(x))
    pt.xlim(0,199)
    pt.yticks([])
    pt.show()
l=[176,79,34,60,92,11,41,114]
h=50
print(scandisk(l,h))