from mathplotlib import pyplot as plt
def fcfs(s,n):
    s1=s.copy()
    s1.insert(0,n)
    se=0
    for i in range(len(s1)-1):
        se+=abs(s1[i]-s1[i+1])
    return se
s=list(map(int,input("enter the sequence: ").split(" ")))
n=int(input("enter the current position of head: "))
print("seek time = ",fcfs(s,n))
