from threading import Thread, Semaphore
NUM_PHILOSOPHERS = 5
forks = [Semaphore(1) for _ in range(NUM_PHILOSOPHERS)]
def philosopher(id):
    left_fork = forks[id]
    right_fork = forks[(id + 1) % NUM_PHILOSOPHERS]
    while True:
        print(f"Philosopher {id} is thinking.")
        left_fork.acquire()
        right_fork.acquire()
        print(f"Philosopher {id} is eating.")
        left_fork.release()
        right_fork.release()
if __name__ == "__main__":
    philosophers = [Thread(target=philosopher, args=(i,)) for i in range(NUM_PHILOSOPHERS)]
    for philosopher in philosophers:
        philosopher.start()
    for philosopher in philosophers:
        philosopher.join()