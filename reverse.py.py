class string_cls:
    def word_rev(self,str):
        l=[w[ : :-1]for w in str.split()]
        return ' '.join(l)
sc=string_cls
str=input('enter a string:')
r_str=sc.word_rev(str)
print(r_str)