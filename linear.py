def linear(l,key):
    flag=0
    p=0
    for i in range(len(l)):
        if l[i]==key:
            flag=1
            p=i
        else:
            pass
    if flag==1:
        print("element to be found at ",p)
    else:
        print("element not found")
l=[]
for i in range(int(input("enter the size:"))):
    l.append(int(input("enter the element:")))
c=linear(l,int(input("enter the element to be found:")))