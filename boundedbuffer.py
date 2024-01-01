from threading import Thread, Semaphore
from collections import deque
BUFFER_SIZE = 10
buffer = deque()
mutex = Semaphore(1)
empty = Semaphore(BUFFER_SIZE)
full = Semaphore(0)
def producer():
    for i in range(20):
        empty.acquire()
        mutex.acquire()
        buffer.append(i)
        mutex.release()
        full.release()
        print("Produced:", i)
def consumer():
    for i in range(20):
        full.acquire()
        mutex.acquire()
        item = buffer.popleft()
        mutex.release()
        empty.release()
        print("Consumed:", item)
Thread(target=producer).start()
Thread(target=consumer).start()