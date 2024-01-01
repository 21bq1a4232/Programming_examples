names=[]
sal=[]
ids=[]
tot=0
for i in range(int(input("enter the number of employees :"))):
    names.append(input("enter the name:"))
    sal.append(float(input("enter sal:")))
    ids.append(input("enter id:"))
for i in range(len(names)):
    if int(input("enter exp: "))<=2:bonus=0
    else:bonus=1000
    tot=tot+sal[i]
    print(names[i],"net salary is :",sal[i]+bonus,"\nemployee name  :",names[i],"\nemployee id :",ids[i],"\nemployee salary :",sal[i])
print("highest sal is :",max(sal),"\nlowest sal is :",min(sal),"\navg sal is :",tot/len(names))