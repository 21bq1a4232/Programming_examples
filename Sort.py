def sort(l):
    h=len(l)
    for i in range(1,h):
        j=i-1
        while l[j]>l[i] and j<i:
            temp=l[i]
            l[i]=l[j]
            l[j]=temp
            j=j+1
            if j==h:
                break
    return l
a=[3,32,45,1,22,2,0]
print(sort(a))




