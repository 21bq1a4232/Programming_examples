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
goal ='F'
v=set()
def dfs(v,g,n):
    if n not in v:
        print(n,end=" ")
        v.add(n)
        for ni in g[n]:
            if goal in v:
                break
            else:
                dfs(v,g,ni)
dfs(v,g,'B')
