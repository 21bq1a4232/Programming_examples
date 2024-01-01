c,j=0,0
l=[]
s=input()
a=input()
while c<=len(s) :
    for i in range(len(s)):
        if i >= j:
            l.append(s[j:i+1])
    c,j=c+1,j+1
for i in l:
    if i==a:
        print(True)
        break
    else:
        print(False)
        break