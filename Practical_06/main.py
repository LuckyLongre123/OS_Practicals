n = int(input("Enter number of processes: "))
b_t = []
index = 0
while index < n:
    b_t.append(int(input("Enter burst time for process " + str(index+1) + ": ")))
    index += 1

w_t = [0] * n
t_t = [0] * n

i = 1
while i < n:
    w_t[i] = w_t[i-1] + b_t[i-1]
    i += 1

i = 0
while i < n:
    t_t[i] = w_t[i] + b_t[i]
    i += 1

print("\nFCFS (First Come First Served) CPU Scheduling")
print("Process\tBurst Time\tWaiting Time\tTurnaround Time")
i = 0
while i < n:
    print(str(i+1) + "\t" + str(b_t[i]) + "\t\t" + str(w_t[i]) + "\t\t" + str(t_t[i]))
    i += 1

avg_wt = sum(w_t) / n
avg_tat = sum(t_t) / n
print("\nAverage Waiting Time: " + str(avg_wt))
print("Average Turnaround Time: " + str(avg_tat))