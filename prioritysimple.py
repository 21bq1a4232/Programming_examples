def priority_non_preemptive(processes, priorities, burst_times):
    num_processes = len(processes)
    completion_times = [0] * num_processes
    waiting_times = [0] * num_processes
    turnaround_times = [0] * num_processes
    for i in range(num_processes):
        max_priority = min(priorities)
        selected_process = priorities.index(max_priority)
        completion_times[selected_process] = sum(completion_times) + burst_times[selected_process]
        waiting_times[selected_process] = sum(completion_times) - sum(waiting_times)
        turnaround_times[selected_process] = completion_times[selected_process] - waiting_times[selected_process]
        priorities[selected_process] = float('inf')
    average_waiting_time = sum(waiting_times) / num_processes
    average_turnaround_time = sum(turnaround_times) / num_processes
    return completion_times, waiting_times, turnaround_times, average_waiting_time, average_turnaround_time
processes = [1, 2, 3, 4]
priorities = [2, 1, 3, 2]
burst_times = [10, 5, 8, 3]
ct, wt, tt, awt, att = priority_non_preemptive(processes, priorities, burst_times)
print("Process\tPriority\tBurst Time\tCompletion Time\tWaiting Time\tTurnaround Time")
for i in range(len(processes)):
    print(f"{processes[i]}\t\t{priorities[i]}\t\t{burst_times[i]}\t\t{ct[i]}\t\t{wt[i]}\t\t{tt[i]}")
print(f"Average Waiting Time: {awt}")
print(f"Average Turnaround Time: {att}")