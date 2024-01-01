from itertools import permutations
n=input()
l=list(n)
k=[]
t=[]
p=permutations(l)
for i in list(p):
    k.append(i)
for i in k:
    s=''
    for j in i:
        s+=j
        a=int(s)
        t.append(a)
q=[]
for i in t:
    c=0
    for j in range(1,i):
        if i%int(j)==0:
            c+=1
    if c==1:
        q.append(i)
print(max(q))