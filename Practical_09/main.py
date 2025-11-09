processes = [
    {'pid': 1, 'arrival': 0, 'burst': 4, 'priority': 2},
    {'pid': 2, 'arrival': 1, 'burst': 3, 'priority': 1},
    {'pid': 3, 'arrival': 2, 'burst': 1, 'priority': 3},
    {'pid': 4, 'arrival': 3, 'burst': 5, 'priority': 2}
]

completed = []
time = 0
total_waiting = 0
total_turnaround = 0

print("\nPID\tArrival\tBurst\tPriority\tStart\tFinish\tWaiting\tTurnaround")
print("-" * 80)

while len(completed) < len(processes):
    available = [p for p in processes if p['arrival'] <= time and p not in completed]

    if not available:
        time += 1
        continue

    current = min(available, key=lambda x: x['priority'])
    start = time
    finish = time + current['burst']
    waiting = start - current['arrival']
    turnaround = finish - current['arrival']

    total_waiting += waiting
    total_turnaround += turnaround

    print("{}\t{}\t{}\t{}\t\t{}\t{}\t{}\t{}".format(
        current['pid'], current['arrival'], current['burst'], current['priority'],
        start, finish, waiting, turnaround
    ))

    time = finish
    completed.append(current)

n = len(processes)
print("\nAverage Waiting Time: {:.2f}".format(total_waiting / n))
print("Average Turnaround Time: {:.2f}".format(total_turnaround / n))
