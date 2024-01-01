l=[5,4,3,2,1]
for i in range(1,len(l)):
    j=i-1
    c=l[i]
    while j>=0 and c<l[j]:
        l[j+1]=l[j]
        j-=1
    l[j+1]=c
print(l)