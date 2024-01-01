def printPattern(n):
    for i in range(1, n + 1):
        for j in range(i, n):
            print("\t", end = "")
        t = i
        for k in range (1, i + 1):
            print(t,"\t","\t", end = "")
            t = t + n - k
        print()
n = 6
printPattern(n)