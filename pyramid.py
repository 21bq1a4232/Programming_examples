n=int(input())
c=0
for i in range(n):
    print((n-(i+1))*" "+"*"*(i)+"*"*(i+1)+" "*(n-(i+1)))
    c+=1
"""for i in range(n, 1, -1):
    for space in range(0, n-i):
        print("  ", end="")
    for j in range(i, 2*i-1):
        print("* ", end="")
    for j in range(1, i-1):
        print("* ", end="")
    print()"""