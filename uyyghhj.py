S = input()
import string


low = string.ascii_lowercase
cap = string.ascii_uppercase

ans  = ''

for i in S:
    if i in low:
        index = low.index(i)
        # 1-2 = -1+26 = 25
        index = ((index-2)+26)%26
        ans+=low[index]
    elif i in cap:
        index = cap.index(i)
        # 1-2 = -1+26 = 25
        index = ((index-3)+26)%26
        ans+=cap[index]
    else:
        ans+=i

print(ans,end="")