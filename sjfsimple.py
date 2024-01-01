def sjf_non_preemptive(processes, burst_times):
    completion_times = []
    waiting_times = []
    turnaround_times = []
    for i, burst_time in enumerate(sorted(burst_times)):
        completion_time = sum(completion_times) + burst_time
        waiting_time = sum(completion_times) if completion_times else 0
        turnaround_time = completion_time - waiting_time
        completion_times.append(completion_time)
        waiting_times.append(waiting_time)
        turnaround_times.append(turnaround_time)
    avg_waiting_time = sum(waiting_times) / len(waiting_times)
    avg_turnaround_time = sum(turnaround_times) / len(turnaround_times)
    return completion_times, waiting_times, turnaround_times, avg_waiting_time, avg_turnaround_time
processes = [1, 2, 3, 4]
burst_times = [10, 5, 8, 3]
completion_times, waiting_times, turnaround_times, awt, att = sjf_non_preemptive(processes, burst_times)
print("Process\tBurst Time\tCompletion Time\tWaiting Time\tTurnaround Time")
for i in range(len(processes)):
    print(f"{processes[i]}\t\t{burst_times[i]}\t\t{completion_times[i]}\t\t{waiting_times[i]}\t\t{turnaround_times[i]}")
print(f"Average Waiting Time: {awt}")
print(f"Average Turnaround Time: {att}")