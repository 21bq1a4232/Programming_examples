s=input().split(',')#['Paris:Delhi:9945672345','Berlin:Brussels:9456723456']
r=len(s)
a=[]
k=[]
d=[]
q=''
c=0
o=1
t=0
for i in s:
    a.append(i.split(':'))#[['paris','Delhi','9945672345'],['Berlin','Brussels','9456723456']]
for i in a:
    for j in i:
        if j.isalpha():
            if c==0:
                l=list(j)
                k.append(l[0])
                k.append(l[1])
                c=c+1
            elif c==1:
                l=list(j)
                k.append(l[-2])
                k.append(l[-1])
                c=0
            else:
                pass
        elif j.isdigit():
            for e in range(len(j)):
                if e%2==0:
                    t=t+int(j[e])
            d.append(str(t)+str(o))
            o=o+1
            t=0
        else:
            pass
if r==2:
    k.insert(4,str(d[0]))
    k.insert(5,',')
    k.append(str(d[-1]))
    p=''.join(k)
    print(p,end="")
elif r==3:
    k.insert(4,str(d[0]))
    k.insert(5,',')
    k.insert(10,str(d[1]))
    k.insert(11,',')
    k.append(str(d[-1]))
    p=''.join(k)
    print(p,end="")
else:
    pass
#print(d)
#Paris:Delhi:9945672345,Berlin:Brussels:9456723456"""