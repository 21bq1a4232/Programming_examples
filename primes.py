def primes(n=100):
    l=[]
    if(n==1):
        return l
    else:
        for i in range(2,n,1):
            f=0
            for j in range(1,i+1):
                if(i%j==0):
                    f+=1
            if(f==2):
                l.append(i)
    return l
n=int(input('enter a number:'))
l=primes(n)
print('list of primes between 1 and {} are {}'.format(n,l))
l=primes()
print('list of primes between 1 and 100 are {}'.format(l))