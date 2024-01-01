def fcfs(processes, burst_times):
    num_processes = len(processes)
    completion_times = [0] * num_processes
    waiting_times = [0] * num_processes
    turnaround_times = [0] * num_processes
    completion_times[0] = burst_times[0]
    for i in range(1, num_processes):
        completion_times[i] = completion_times[i - 1] + burst_times[i]
        waiting_times[i] = completion_times[i - 1]
        turnaround_times[i] = completion_times[i]
    average_waiting_time = sum(waiting_times) / num_processes
    average_turnaround_time = sum(turnaround_times) / num_processes
    return completion_times, waiting_times, turnaround_times, average_waiting_time, average_turnaround_time
processes = [1, 2, 3, 4]
burst_times = [10, 5, 8, 3]
completion_times, waiting_times, turnaround_times, avg_waiting_time, avg_turnaround_time = fcfs(processes, burst_times)
print("Process\tBurst Time\tCompletion Time\tWaiting Time\tTurnaround Time")
for i in range(len(processes)):
    print(f"{processes[i]}\t\t{burst_times[i]}\t\t{completion_times[i]}\t\t{waiting_times[i]}\t\t{turnaround_times[i]}")
print(f"Average Waiting Time: {avg_waiting_time}")
print(f"Average Turnaround Time: {avg_turnaround_time}")