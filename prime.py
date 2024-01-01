k=[]
l=[1,2,3,4,5,6,7,8,9,10,11,12]
for i in l:
    c=0
    for j in range(1,len(l)+1):
        if i%j==0:
            c+=1
    if c==2:
        k.append(i)
    else:
        pass
print(k)