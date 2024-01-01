def iterative(l,n,key):
    for i in range(n):
        if l[i]==key:
            return i
        elif i==n-1:
            return -1
def recursive(l,n,key,x=0):
    '''if i:
        pass
    else:
        i=0'''
    if x>n:
        return -1
    else:
        if key==l[x]:
            return x
        else:
            return recursive(l,n,key,x+1)
        
n=int(input())
l=[]
for i in range(n):
  l.append(int(input()))
key=int(input())
a=int(input('enter the choice 1.Iteration''\n''2.Other'))
if a==1:
    res=iterative(l,n,key)
else :
    res=recursive(l,n,key)
if res==-1:
    print("element not found")
else:
    print("index is:",res)