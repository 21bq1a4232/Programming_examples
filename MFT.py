totalmem=int(input("enter total ammount of memory"))
blocksize=int(input("enter the block size"))
noofblocks=totalmem//blocksize
print(noofblocks)
ef=totalmem-(noofblocks*blocksize)
nop=int(input("enter the number of the processes"))
processlist=[0]*nop
for i in range(nop):
    processlist[i]=int(input("enter the ammount of memory required for the process"))
print(processlist)
print("PROCESS\tMEMORYREQUIRED\tALLOCATED\tINTERNALFRAGMENTATION")
totalif=0
blockallocated=0
for i in range(nop):
    if(blockallocated<noofblocks):
            print("p",i,end="\t\t")
            print(processlist[i],end="\t\t")
            if(processlist[i]>blocksize):
                print("NO")
            else:
                print("YES",end="\t\t")
                print(blocksize-processlist[i])
                totalif=totalif+(blocksize-processlist[i])
                blockallocated=blockallocated+1
    else:
            print("\nMemory is Full, Remaining Processes cannot be accomodated");
print("\n\nTotal Internal Fragmentation is",totalif)
print("\nTotal External Fragmentation is",ef)