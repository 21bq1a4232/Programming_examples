import threading
class Philosopher(threading.Thread):
    def __init__(self, name, left_chopstick, right_chopstick):
        super().__init__()
        self.name = name
        self.left_chopstick = left_chopstick
        self.right_chopstick = right_chopstick
    def run(self):
        while True:
            self.think()
            self.eat()
    def think(self):
        print(f"{self.name} is thinking.")
    def eat(self):
        with self.left_chopstick, self.right_chopstick:
            print(f"{self.name} is eating.")
num_philosophers = 5
chopsticks = [threading.Lock() for _ in range(num_philosophers)]
philosophers = [Philosopher(f"Philosopher {i+1}", chopsticks[i], chopsticks[(i + 1) % num_philosophers])
               for i in range(num_philosophers)]
for philosopher in philosophers:
    philosopher.start()
for philosopher in philosophers:
    philosopher.join()