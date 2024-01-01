import threading
import time
import random
class Philosopher(threading.Thread):
    running = True
    def __init__(self, index, left_fork, right_fork):
        threading.Thread.__init__(self)
        self.index = index
        self.left_fork = left_fork
        self.right_fork = right_fork
    def run(self):
        while self.running:
            print(f"Philosopher {self.index+1} is thinking.\n")
            time.sleep(random.uniform(1,2))
            print(f"Philosopher {self.index+1} is hungry.\n")
            self.left_fork.acquire()
            locked = self.right_fork.acquire(timeout=5)
            if not locked:
                self.left_fork.release()
                print(f"Philosopher {self.index+1} couldn't pick up the right fork. Retrying later.\n")
                continue
            print(f"Philosopher {self.index+1} is eating.\n")
            time.sleep(random.uniform(1,2))
            self.right_fork.release()
            self.left_fork.release()
        print(f"Philosopher {self.index+1} has finished eating and thinking.\n")
forks = [threading.Lock() for _ in range(5)]
philosophers = [Philosopher(i, forks[i], forks[(i + 1) % 5]) for i in range(5)]
Philosopher.running = True
for philosopher in philosophers:
    philosopher.start()
time.sleep(3)
Philosopher.running = False
for philosopher in philosophers:
    philosopher.join()