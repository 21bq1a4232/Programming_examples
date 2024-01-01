def sjf_scheduling(arrival_time, burst_time):
    completion_time = []
    turnaround_time = []
    waiting_time = []
    for i in range(len(arrival_time)):
        completion_time.append(sum(burst_time[:i+1]))
        turnaround_time.append(completion_time[i] - arrival_time[i])
        waiting_time.append(turnaround_time[i] - burst_time[i])
    return completion_time, turnaround_time, waiting_time
arrival_time = [0, 2, 4, 6]
burst_time = [8, 4, 2, 6]
completion, turnaround, waiting = sjf_scheduling(arrival_time, burst_time)
print("Completion Time:", completion)
print("Turnaround Time:", turnaround)
print("Waiting Time:", waiting)