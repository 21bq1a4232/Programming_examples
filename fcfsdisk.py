import matplotlib.pyplot as plt
def fcfs_disk_scheduling(arr, head):
    total_seek_time = 0
    current_track = head
    seek_sequence = []
    for track in arr:
        seek_sequence.append(current_track)
        total_seek_time += abs(track - current_track)
        current_track = track
        seek_sequence.append(current_track)
    return total_seek_time, seek_sequence
requests = [79,110,50,38,40,120]
initial_head = 50
seek_time, seek_sequence = fcfs_disk_scheduling(requests, initial_head)
print("Total Seek Time:", seek_time)
plt.plot(seek_sequence, range(len(seek_sequence)), marker='o')
plt.xlabel('Track')
plt.ylabel('Time')
plt.title('FCFS Disk Scheduling')
plt.grid(True)
plt.show()