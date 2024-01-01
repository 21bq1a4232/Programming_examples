from random import randint
def fcfs(processes):
    #processes.sort(key=lambda x:x['pr'])
    ct=0
    twt=0
    for p in processes:
        wt=max(ct-p['at'],0)
        ct+=p['bt']
        twt+=wt
    awt=twt/len(processes)
    return awt
processes=[]
for i in range(5):
    processes.append({
        'at':randint(0,10),'bt':randint(1,11)})
for p in processes:
    print(p)
print(fcfs(processes))