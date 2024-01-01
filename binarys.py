def binary_search(l,low,high,key):
    while low<=high:
        mid=(low+high)//2
        if l[mid]==key:
            return mid
        elif[mid]==key:
            high=mid-1
        else:
            low=mid+1
        return-1
lst=[]
n=int(input("enter number of elements:"))
a=0
h=n-1
for i in range(n):
    ele=(input("enter element:"))
    lst.append(ele)
keys=int(input("enter element to be found:"))
result=binary_search(list,a,h,keys)
if result==-1:
    print("element not found")
else:
    print("element is found at index:",result)