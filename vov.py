def replaceV(S):
  vowels=list("aeiouAEIOU")
  L=list(S)
  for i in range(len(L)-2):
    if L[i] in vowels and L[i+1] in vowels and L[i+2] in vowels:
      L[i]='*'
      L[1+i]="*"
      L[i+2]="*"
      i+=2
  return("".join(L).replace("***","_"))
print(replaceV(input()),end="")