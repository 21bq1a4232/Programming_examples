def tower(n,b,m,e):
    if n==1:
        print("move disk 1 from pole {} to pole {}".format(b,e))
        return
    tower(n-1,b,e,m)
    print("move disk {}	 from pole {} to pole {}".format(n,b,e))
    tower(n-1,m,b,e)
n=3
tower(n,'A','B','C')