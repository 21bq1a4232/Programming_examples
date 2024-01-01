try:
    x=input('Enter a value:')
    x=int(x)+1
    print(x)
except ValueError:
    print('please give valid integer')
else:
    print('success,no error')