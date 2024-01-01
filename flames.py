x=input()
y=input()
x=list(x)
y=list(y)
for i in x:
    for j in y:
        if i==j:
            x.remove(i)
            y.remove(j)
for j in range(len(y)):
    x.append(y[j])
x=set(x)
x=list(x)
l=['f','l','a','m','e','s']
n=len(x)
  for i in range(len(l)):
      if i==len(l)-1:
        print(l[i])
      else:
         l.pop(i)
         l.pop(i)