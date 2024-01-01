from matplotlib import pyplot as plt
def fcfs(s,st):
    t=s.copy()
    t.insert(0,st)
    plt.rcParams['xtick.bottom'] = plt.rcParams['xtick.labelbottom']=False
    plt.rcParams['xtick.top'] = plt.rcParams['xtick.labeltop'] = True
    sz=len(t)
    x=t
    y=[]
    headm=0
    for i in range(0,sz):
        y.append(-i)
        if i!= sz-1:
            headm+=abs(t[i]-t[i-1])
        string="headMoment = ",str(headm)
        string2=str(t)
        print(headm)
    plt.plot(x,y,color="purple",markerfacecolor="blue",marker="o",markersize=5,linewidth=2,label="fcfs")
    plt.ylim = (0 ,sz)
    plt.yticks([])
    plt.xlim = (0 , 199)
    plt.title("fcfs")
    plt.show()
print("seek time = ",fcfs(list(map(int,input("enter the sequence: ").split(" "))),int(input("enter the current position of head:"))))
