l=[]
n=int(input())
for i in range(n):
    l.append(int(input()))
m=int(input('enter the index:'))
try:
    print(l[m])
except :
    print('index out of range')
else:
    print(l[m])
finally:
    print("end of program")