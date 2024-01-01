def isPalindrome(s):
    s=s.lower()
    q=[' ',',']
    s=s.replace(' ','')
    s=s.replace(',','')
    
    s=s.replace(':','')
    print(s)
    if s==s[::-1]:
            #print(s.lower(),"\n",s[::-1].lower())
        return True
    else:
        return False
print(isPalindrome("A man, a plan, a canal: Panama"))