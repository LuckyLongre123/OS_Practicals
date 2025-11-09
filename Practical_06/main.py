processes = [
    {'pid': 1, 'arrival': 0, 'burst': 5},
    {'pid': 2, 'arrival': 1, 'burst': 3},
    {'pid': 3, 'arrival': 2, 'burst': 8},
    {'pid': 4, 'arrival': 3, 'burst': 6}
]
processes.sort(key=lambda x: x['arrival'])

current_time = 0
total_waiting = 0
total_turnaround = 0

print("\nPID\tArrival\tBurst\tStart\tFinish\tWaiting\tTurnaround")
print("-" * 70)

for p in processes:
    if current_time < p['arrival']:
        current_time = p['arrival']
    start_time = current_time
    finish_time = current_time + p['burst']
    waiting_time = start_time - p['arrival']
    turnaround_time = finish_time - p['arrival']
    total_waiting += waiting_time
    total_turnaround += turnaround_time
    print("{}\t{}\t{}\t{}\t{}\t{}\t{}".format(
        p['pid'], p['arrival'], p['burst'],
        start_time, finish_time, waiting_time, turnaround_time
    ))
    current_time = finish_time

n = len(processes)
print("\nAverage Waiting Time: {:.2f}".format(total_waiting / n))
print("Average Turnaround Time: {:.2f}".format(total_turnaround / n))
