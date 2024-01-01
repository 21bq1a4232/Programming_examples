np=[]
c=0
mname=input("enter the movie name:")
nt=int(input("enter the no of tickets,provided less then 7:"))
if nt<7:
    for i in range(nt):
        p=input("enter the name of the person:")
        np.append(p)
        s=len(np)
    print("there are 100 seats\n1-30-premium seats-300 per hand\n40-70-1st class\n70-100-2nd class-70")
    n=int(input("enter the seats of your choice:"))
    print(mname)
    if n<31:
        c=nt*300
        from random import randint
        print("the total cost including gst is ",c+75.26)
        for i in np:
            seat=randint(1,30)
            print(i,seat)
    elif n<71:
        c=nt*150
        print("the total cost including gst is ",c+75.26)
        for i in np:
            seat=randint(31,70)
            print(i,seat,c)
    elif n<101:
        c=nt*70
        print("the total cost including gst is ",c+75.26)
        for i in np:
            seat=randint(71,100)
            print(i,seat,c)
    else:
        print("please enter a valid choice")