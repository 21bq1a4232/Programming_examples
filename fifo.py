def fifi(p,c):
    m=[]
    pg=0
    for i in p:
        if i not in m:
            pg+=1
            if len(m) < c :
                m.append(i)
            else:
                m.pop(0)
                m.append(i)
    return pg
pages = list(map(int,input("enter the input sequeses").split()))
cap=int(input())
print(fifi(pages,cap))