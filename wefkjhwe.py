c,j=0,0
l=[]
s=input()
while c<=len(s) :
    for i in range(len(s)):
        if i >= j:
            l.append(s[j:i+1])
        #    print(l)
    j+=1
    c+=1
print(l)