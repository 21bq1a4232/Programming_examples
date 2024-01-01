n=int(input())
nooftowers=int(input())
l=(list(map(int,input().split(" "))))
k1=(int(input()))
k=(list(map(int,input().split())))
a=l[0]
for i in range(nooftowers):
    if (a+1)==l[i]:
        a=l[i]
    else:
        if a==l[i]:
            l[i]+=0
        else:
            l[i]+=1
print(l)