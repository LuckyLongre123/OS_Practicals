num_processes = int(input("Enter number of processes: "))
burst_times = []
index = 0
while index < num_processes:
    burst_times.append(int(input("Enter burst time for process " + str(index+1) + ": ")))
    index += 1

process_ids = list(range(1, num_processes + 1))
i = 0
while i < num_processes:
    j = i + 1
    while j < num_processes:
        if burst_times[i] > burst_times[j]:
            burst_times[i], burst_times[j] = burst_times[j], burst_times[i]
            process_ids[i], process_ids[j] = process_ids[j], process_ids[i]
        j += 1
    i += 1

waiting_times = [0] * num_processes
turnaround_times = [0] * num_processes

i = 1
while i < num_processes:
    waiting_times[i] = waiting_times[i - 1] + burst_times[i - 1]
    i += 1

i = 0
while i < num_processes:
    turnaround_times[i] = waiting_times[i] + burst_times[i]
    i += 1

print("\nSJF (Shortest Job First) CPU Scheduling")
print("Process\tBurst Time\tWaiting Time\tTurnaround Time")
i = 0
while i < num_processes:
    print(str(process_ids[i]) + "\t" + str(burst_times[i]) + "\t\t" + str(waiting_times[i]) + "\t\t" + str(turnaround_times[i]))
    i += 1

avg_wt = sum(waiting_times) / num_processes
avg_tat = sum(turnaround_times) / num_processes
print("\nAverage Waiting Time: " + str(avg_wt))
print("Average Turnaround Time: " + str(avg_tat))