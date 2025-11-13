num_processes = int(input("Enter number of processes: "))
burst_times = []
index = 0
while index < num_processes:
    burst_times.append(int(input("Enter burst time for process " + str(index+1) + ": ")))
    index += 1

waiting_times = [0] * num_processes
turnaround_times = [0] * num_processes

i = 1
while i < num_processes:
    waiting_times[i] = waiting_times[i-1] + burst_times[i-1]
    i += 1

i = 0
while i < num_processes:
    turnaround_times[i] = waiting_times[i] + burst_times[i]
    i += 1

print("\nFCFS (First Come First Served) CPU Scheduling")
print("Process\tBurst Time\tWaiting Time\tTurnaround Time")
i = 0
while i < num_processes:
    print(str(i+1) + "\t" + str(burst_times[i]) + "\t\t" + str(waiting_times[i]) + "\t\t" + str(turnaround_times[i]))
    i += 1

avg_wt = sum(waiting_times) / num_processes
avg_tat = sum(turnaround_times) / num_processes
print("\nAverage Waiting Time: " + str(avg_wt))
print("Average Turnaround Time: " + str(avg_tat))