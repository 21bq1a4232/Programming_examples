def recursion(l):
    q=[]
    for i in l:
        q.append(int(i))
    a=max(q)
    if a==q[0]:
        print('Setter')
    elif a==q[1]:
        print('Tester')
    elif a==q[2]:
        print('Editorialist')
    else:
        pass
n=int(input())
l=[]
for i in range(n):
    l.append(input())
s=''
for i in l:
    s+=i
s=s.replace(' ','')
s=[s[i:i + 3] for i in range(0, len(s), 3)]
for i in s:
    recursion(i)