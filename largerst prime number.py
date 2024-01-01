from itertools import permutations
def prime(l):
    k=[]
    for i in l:
        c=0
        for j in range(1,i):
            if i%j==0:
                c+=1
        if c==1:
            k.append(i)
        else:
            pass
    return k
s=int(input())
p=permutations(str(s))
l=[]
for i in p:
    l.append(int(''.join(i)))
k=prime(l)
print(max(k))