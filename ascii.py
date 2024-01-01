k=[]
ck=[]
s=input()
for i in s:
    c=0
    for j in s:
        if i==j:
            c+=1
    if c%2==0:
        pass
    else:
        k.append(i)
        ck.append(c)
a=ck.index(max(ck))
print(ord(k[a]))