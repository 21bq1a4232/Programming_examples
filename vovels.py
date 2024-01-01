#if __name__=='__main__':
    s=input()
    i=0
    l=['a','e','o','i','u']
    if s[i]=='a' or s[i]=='e' or s[i]=='o' or s[i]=='i' or s[i]=='u':
        if s[i:i+3]=='aaa' :
            s.replace('aaa','_')
            i+=1
        elif s[i:i+3]=='eee':
            s.replace('eee','_')
            i+=1
        elif s[i:i+3]=='ooo':
            s.replace('ooo','_')
            i+=1
        elif s[i:i+3]=='iii':
            s.replace('iii','_')
            i+=1
        elif s[i:i+3]=='uuu':
            s.replace('iii','_')
            i+=1
        else:
            i+=1
    print(s)