def test(word):
    new_word = ''
    for ch in word:
        if ch>='a' and ch<='z':
            temp = ord (ch)
            temp = temp - 32
            temp = chr(temp)
            new_word = new_word + temp
    return new_word
n=input()
print(test(n))