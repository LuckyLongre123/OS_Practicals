processes = [
    {'pid': 1, 'arrival': 0, 'burst': 8, 'remaining': 8},
    {'pid': 2, 'arrival': 1, 'burst': 4, 'remaining': 4},
    {'pid': 3, 'arrival': 2, 'burst': 9, 'remaining': 9},
    {'pid': 4, 'arrival': 3, 'burst': 5, 'remaining': 5}
]

time = 0
completed = 0
n = len(processes)
total_waiting = 0
total_turnaround = 0
completion = {}

while completed < n:
    available = [p for p in processes if p['arrival'] <= time and p['remaining'] > 0]

    if not available:
        time += 1
        continue

    current = min(available, key=lambda x: x['remaining'])
    current['remaining'] -= 1
    time += 1

    if current['remaining'] == 0:
        completed += 1
        finish = time
        turnaround = finish - current['arrival']
        waiting = turnaround - current['burst']
        total_waiting += waiting
        total_turnaround += turnaround
        completion[current['pid']] = (finish, waiting, turnaround)

print("\nPID\tArrival\tBurst\tFinish\tWaiting\tTurnaround")
print("-" * 60)

for p in processes:
    f, w, t = completion[p['pid']]
    print("{}\t{}\t{}\t{}\t{}\t{}".format(p['pid'], p['arrival'], p['burst'], f, w, t))

print("\nAverage Waiting Time: {:.2f}".format(total_waiting / n))
print("Average Turnaround Time: {:.2f}".format(total_turnaround / n))
