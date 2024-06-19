def round_robin(burst_times, quantum):
    processes = [f"p{i + 1}" for i in range(len(burst_times))]
    num_processes = len(processes)
    wait_time = [0] * num_processes
    remaining_time = burst_times.copy()
    time = 0
    gantt_chart = []

    while any(remaining_time):
        for i in range(num_processes):
            current_time = min(quantum, remaining_time[i])
            if current_time > 0:
                gantt_chart.append((time, processes[i], time + current_time))
                time += current_time
                remaining_time[i] -= current_time
                wait_time[i] = time - burst_times[i]

    avg_wait_time = sum(wait_time) / num_processes
    return avg_wait_time, gantt_chart

num_processes = int(input("enter number of process: "))
burst_times = [int(input(f"enter burst time for process {i + 1}: ")) for i in range(num_processes)]
quantum = int(input("enter quantum: "))

avg_wait_time, gantt_chart = round_robin(burst_times, quantum)

print("\ngantt chart:")
for entry in gantt_chart:
    print(entry[0], entry[1], entry[2], end="|")

print(f"\n\naverage waiting time = {avg_wait_time:.0f} ms")
