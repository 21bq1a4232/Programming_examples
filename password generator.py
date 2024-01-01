import array
import random
l=''
for i in range(97,97+26):
    l=l+chr(i)
k=l.upper()
n=''
for i in range(10):
    n=n+str(i)
l=list(l)
k=list(k)
n=list(n)
s = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
           '*', '(', ')', '<']
c=l+k+n+s
rl=random.choice(l)
rk=random.choice(k)
rn=random.choice(n)
rs=random.choice(s)
temp=rl+rk+rn+rs
for i in range(4):
    temp=temp+random.choice(c)
    temp1=array.array('u',temp)
    random.shuffle(temp1)
password=''
for i in temp1:
    password+=i
print(password)
cl=0
ck=0
cs=0
for h in password:
    if h in l:
        cl=1
    if h in k:
        ck=1
    if h in s:
        cs=1
if cl ==1 and ck==1 and cs==1:
    print("strong")
elif (cl == 1 and ck==1) or (ck==1 and cs==1) or (cl==1 and cs==1):
    print('better')
else:
    print('weak')