n=int(input())
fact=1
if n==0:
    fact=1
else:
    while(n!=0):
        fact*=n
        n=n-1
print(fact)