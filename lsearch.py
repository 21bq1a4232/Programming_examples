n=int(input())
l=[]
for i in range(n):
  l.append(int(input()))
key=int(input())
for i in range(len(l)):
  if key==l[i]:
    print('index of key is:',i)
    break
  else:
      continue
if len(l)==i:
  print('element not found')


  
