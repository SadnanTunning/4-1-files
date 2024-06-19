def avg_wt_time(bts, priorities):
    n = len(bts)
    wts = [sum(bts[j] for j in range(n) if priorities[j] < priorities[i]) for i in range(n)]
    avg_wt = float(sum(wts) / n)
    return wts, avg_wt

def display_gantt_chart(processes):
    gantt_chart = "0"
    for burst_time, _, process_id in processes:
        gantt_chart += f"  {process_id} {burst_time + int(gantt_chart.split()[-1])}"
    print("\ngantt Chart:")
    print(gantt_chart.replace("|  ", "| ").replace("  ", " "))

def priority_scheduling(bts, priorities):
    processes = sorted(zip(bts, priorities, [f'P{i}' for i in range(1, len(bts) + 1)]), key=lambda x: x[1])
    return processes

def main():
    bts = []
    priorities = []
    num_processes = int(input("enter number of process: "))

    for i in range(num_processes):
        burst_time = int(input(f"enter burst time for process {i + 1}: "))
        priority = int(input(f"enter priority for process {i + 1}: "))
        bts.append(burst_time)
        priorities.append(priority)

    processes = priority_scheduling(bts, priorities)
    display_gantt_chart(processes)

    _, avg_waiting_time = avg_wt_time(bts, priorities)
    print("\naverage waiting time =", avg_waiting_time, "ms")

if __name__ == "__main__":
    main()