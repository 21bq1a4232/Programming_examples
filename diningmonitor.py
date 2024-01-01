import threading
class DiningPhilosophersMonitor:
    def __init__(self, num_philosophers):
        self.chopsticks = [threading.Condition() for _ in range(num_philosophers)]
    def pick_up_chopsticks(self, philosopher_id):
        left, right = philosopher_id, (philosopher_id + 1) % len(self.chopsticks)
        with self.chopsticks[left], self.chopsticks[right]:
            while any(self.chopsticks[i].locked() for i in (left, right)):
                for chopstick in (left, right):
                    self.chopsticks[chopstick].wait()
    def put_down_chopsticks(self, philosopher_id):
        left, right = philosopher_id, (philosopher_id + 1) % len(self.chopsticks)
        with self.chopsticks[left], self.chopsticks[right]:
            for chopstick in (left, right):
                self.chopsticks[chopstick].notify()
class Philosopher(threading.Thread):
    def __init__(self, name, philosopher_id, monitor):
        super().__init__()
        self.name = name
        self.philosopher_id = philosopher_id
        self.monitor = monitor
    def run(self):
        while True:
            self.think()
            self.eat()
    def think(self):
        print(f"{self.name} is thinking.")
    def eat(self):
        self.monitor.pick_up_chopsticks(self.philosopher_id)
        print(f"{self.name} is eating.")
        self.monitor.put_down_chopsticks(self.philosopher_id)
num_philosophers = 5
monitor = DiningPhilosophersMonitor(num_philosophers)
philosophers = [Philosopher(f"Philosopher {i+1}", i, monitor) for i in range(num_philosophers)]
for philosopher in philosophers:
    philosopher.start()
for philosopher in philosophers:
    philosopher.join()