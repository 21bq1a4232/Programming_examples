def Binary(lst,key):// this is a function
    l=0
    h=len(lst)-1
    while l<=h:
        mid=(l+h)//2
        if lst[mid]==key:
            print("element found at ",mid)
            break
        elif lst[mid]>mid:
            l=mid+1
        else:
            h=mid-1
    if l>h:
        print("element not found")
l=[]
for i in range(int(input("enter the size of an array:"))):
    l.append(int(input("enter the element :")))
Binary(l,int(input("enter the element to be found")))
