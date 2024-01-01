from collections import deque
def round_robin(processes, time_quantum):
    queue = deque(processes)
    total_waiting_time = 0
    while queue:
        process = queue.popleft()
        if process > time_quantum:
            queue.append(process - time_quantum)
            total_waiting_time += time_quantum
        else:
            total_waiting_time += process
    avg_waiting_time = total_waiting_time / len(processes)
    print(f"Average Waiting Time: {avg_waiting_time:.2f}")
processes = [12, 6, 8, 3, 10]
time_quantum = 4
round_robin(processes, time_quantum)