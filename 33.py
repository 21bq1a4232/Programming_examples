try:
    f_name=input('enter file name:')
    fp=open(f_name)
    print('file opened')
    print('contents are \n ',fp.read())
except FileNotFoundError:
    print('file does not exists')
finally:
    fp.close()
    print('file successfully closed')