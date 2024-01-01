l=[5,4,3,2,1]
for i in range(len(l)):
    for j in range(1,len(l)):
        if l[j]<l[j-1]:
            temp=l[j]
            l[j]=l[j-1]
            l[j-1]=temp
print(l)