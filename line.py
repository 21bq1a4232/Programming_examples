l=[1,2,3,4,5,6,7,8,9]
l=set(l)
l=list(l)
l.sort()
p=int(input("enter the element required:"))
for i in range(len(l)):
    if l[i]==p:
        print("element found at index:",i)
        break
else:
    print("element not found")