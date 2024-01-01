def merge(l1,l2):

    for i in range(len(l1)):
        for j in range(i):
            l1.append(l2[j])    
        
    return l1+l2
a=merge([1],[1,2,6,7,'a',4,5,3,4])
print(a)
