def merge(l1,l2):
  l=[]
  l=l1+l2
  l.sort()
  return(l)
l1=[]
l2=[]
n=int(input('enter the len of l1:'))
m=int(input('enter the len of l2:'))
for i in range(n):
    l1.append(int(input()))
for i in range(m):
    l2.append(int(input()))   
l1.sort()
l2.sort()
l=merge(l1,l2)
s=set(l)
l=list(s)
print('the merged list is',*l)