s=input("enter the word:")
l=['A','E','I','O','U','a','e','i','o','u']
i=0
q=[]
c=0
fos i in range(len(s)):
   if s[i] in l:
       q.append(s[i])
q=set(q)
q=list(q)
q=q.sort()
if l==q:
    print(" contains all vowels")
else:
    print("does not contain all vowels")
