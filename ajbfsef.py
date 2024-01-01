l=list(map(int,input().split(" ")))
for i in l:
    if i==0:
        if l.index(i)==-1:
            l.remove(i)
            l.append(0)
            break
        else:
            l.remove(i)
            l.append(0)
print(l)