def fcfs_cpu_scheduling(arrival_time, burst_time):
    completion_time = [sum(burst_time[:i+1]) for i in range(len(arrival_time))]
    turnaround_time = [completion_time[i] - arrival_time[i] for i in range(len(arrival_time))]
    waiting_time = [turnaround_time[i] - burst_time[i] for i in range(len(arrival_time))]
    return completion_time, turnaround_time, waiting_time
arrival_time = [0, 2, 4, 6]
burst_time = [8, 4, 2, 6]
completion, turnaround, waiting = fcfs_cpu_scheduling(arrival_time, burst_time)
print("Completion Time:", completion)
print("Turnaround Time:", turnaround)
print("Waiting Time:", waiting)