import threading
import time
CAPACITY = 10
buffer = [-1 for i in range(CAPACITY)]
in_index = 0
out_index = 0
mutex = threading.Semaphore()
empty = threading.Semaphore(CAPACITY)
full = threading.Semaphore(0)
class Producer(threading.Thread):
  def run(self):
    global CAPACITY, buffer, in_index, out_index
    global mutex, empty, full
    items_produced=0
    counter=0
    while items_produced < 20:
      empty.acquire()
      mutex.acquire()
      counter += 1
      buffer[in_index] = counter
      in_index = (in_index + 1)%CAPACITY
      print("Producer produced : ", counter)
      mutex.release()
      full.release()
      time.sleep(1)
      items_produced += 1
class Consumer(threading.Thread):
  def run(self):
    global CAPACITY, buffer, in_index, out_index, counter
    global mutex, empty, full
    items_consumed = 0
    while items_consumed < 20:
      full.acquire()
      mutex.acquire()
      item = buffer[out_index]
      out_index = (out_index + 1)%CAPACITY
      print("Consumer consumed item : ", item)
      mutex.release()
      empty.release()      
      time.sleep(2.5)
      items_consumed += 1
producer = Producer()
consumer = Consumer()
consumer.start()
producer.start()
producer.join()
consumer.join()