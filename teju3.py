n=int(input())
for k in range(2):
    for i in range(n):
        for j in range(i+1):
            print('*',end=" ")
        print()