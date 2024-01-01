l=[]
n=int(input("enter the size of the array:"))
for i in range(n):
    s=int(input("enter the element:" ))
    l.append(s)
x=int(input("enter element to search:"))
f=0
for i in range(len(l)):
    if x==l[i]:
        f=1
        print("element fount at position:",i)
        break
    else:
        i=i+1
if f==0:
    print("elements not found")