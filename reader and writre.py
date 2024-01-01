import threading as thread
import random
global x
x=0
lock=thread.Lock()
def reader():
    global x
    print("reader is reading")
    lock.acquire()
    print("shared data :",x,"\n")
    lock.release()
    print()
def writer():
    global x
    print("writer is writing")
    lock.acquire()
    x+=1
    print("writer is releasing the lock")
    lock.release()
    print()
for i in range(10):
    r=random.randint(0,100)
    if r>50:
        t1=thread.Thread(target=reader)
        t1.start()
    else:
        t2=thread.Thread(target=writer)
        t2.start()
t1.join()
t2.join()