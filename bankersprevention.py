class BankerPrevention:
    def __init__(self, allocation, max_need, available):
        self.num_processes = len(allocation)
        self.num_resources = len(available)
        self.allocation = allocation
        self.max_need = max_need
        self.available = available
        self.need = [[max_need[i][j] - allocation[i][j] for j in range(self.num_resources)] for i in range(self.num_processes)]
    def is_safe_state(self):
        work = self.available[:]
        finish = [False] * self.num_processes
        safe_sequence = []
        while True:
            found = False
            for i in range(self.num_processes):
                if not finish[i] and all(need <= work[j] for j, need in enumerate(self.need[i])):
                    work = [work[j] + self.allocation[i][j] for j in range(self.num_resources)]
                    finish[i] = True
                    safe_sequence.append(i)
                    found = True
            if not found:
                break
        if all(finish):
            print("System is in a safe state.")
            print("Safe sequence:", safe_sequence)
            return True
        else:
            print("System is not in a safe state.")
            return False
allocation = [[0, 1, 0], [2, 0, 0], [3, 0, 2], [2, 1, 1], [0, 0, 2]]
max_need = [[7, 5, 3], [3, 2, 2], [9, 0, 2], [2, 2, 2], [4, 3, 3]]
available = [3, 3, 2]
banker = BankerPrevention(allocation, max_need, available)
banker.is_safe_state()