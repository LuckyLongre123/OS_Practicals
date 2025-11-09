processes = [
    {'pid': 1, 'arrival': 0, 'burst': 6},
    {'pid': 2, 'arrival': 1, 'burst': 8},
    {'pid': 3, 'arrival': 2, 'burst': 7},
    {'pid': 4, 'arrival': 3, 'burst': 3}
]

completed = []
time = 0
total_waiting = 0
total_turnaround = 0

print("\nPID\tArrival\tBurst\tStart\tFinish\tWaiting\tTurnaround")
print("-" * 70)

while len(completed) < len(processes):
    available = [p for p in processes if p['arrival'] <= time and p not in completed]

    if not available:
        time += 1
        continue

    current = min(available, key=lambda x: x['burst'])
    start = time
    finish = time + current['burst']
    waiting = start - current['arrival']
    turnaround = finish - current['arrival']

    total_waiting += waiting
    total_turnaround += turnaround

    print("{}\t{}\t{}\t{}\t{}\t{}\t{}".format(
        current['pid'], current['arrival'], current['burst'],
        start, finish, waiting, turnaround
    ))

    time = finish
    completed.append(current)

n = len(processes)
print("\nAverage Waiting Time: {:.2f}".format(total_waiting / n))
print("Average Turnaround Time: {:.2f}".format(total_turnaround / n))
