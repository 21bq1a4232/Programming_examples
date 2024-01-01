def asum(l):
    i=0
    sum=0
    if i<len(l):
        sum+=asum(l)
    i+=1
    return sum
    
a=sum([1,2,3,4])
print(a)
