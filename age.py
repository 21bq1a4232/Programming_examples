try:
    age=int(input('enter age of a person:'))
    if age<21:
        raise ValueError('Invalid age')
    else:
        pass
except ValueError as e:
    print(e)
else:
    print('you are eligible for vote')