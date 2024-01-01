def capital(a):
    i=0
    s=''
    for x in a:
        if ord(x)>64 and ord(x)<97:
            continue
        else:
            x=ord(x)
            x-=32
        s=s+chr(x)
        i+=1
    return s
a=capital('abcde') 
print(a)
