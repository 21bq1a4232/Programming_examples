def anagram(b,k):
    for i in range(len(k)):
        if b==k[i]:
            return 1
from itertools import permutations
a=input()
b=input()
p=permutations(a)
l=list(p)
k=[]
q=[]
for i in l:
    k.append("".join(i))
r=anagram(b,k)
if r==1:
    print("both of them are anagrams")
else:
    print("they are not anagrams")