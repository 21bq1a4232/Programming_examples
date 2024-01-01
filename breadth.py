g={
    'A':['B','D'],
    'B':['C','E','G'],
    'C':['A'],
    'D':['C'],
    'E':['H'],
    'F':[],
    'G':['F'],
    'H':['G','F']
}
v=[]
q=[]
def bfs(v,g,n,q):
    v.append(n)
    q.append(n)
    while q:
        m=q.pop(0)
        print(m,end="  ")
        for ni in g[m]:
            if ni not in v:
                v.append(ni)
                q.append(ni)
bfs(v,g,'A',q)