def square(l):
    a=[]
    for i in l:
        a.append(i*i)
    return l+a 
l=list(map(int,input().split(" ")))
t=square(l)
t=tuple(t)
print(t)