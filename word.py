from itertools import permutations
st=input('enter a word:')
for i in range(2,len(st)):
    for p in permutations(st,i):
       print(' '.join(p),end='')
    print()
