def avg_wt_time(bts):
    wts = [0]
    avg_wt = 0

    for j in range(1, len(bts)):
        wt = wts[j - 1] + bts[j - 1]
        wts.append(wt)
        avg_wt += wt

    avg_wt = float(avg_wt / len(bts))
    return wts, avg_wt

def display_info(wts, bts, avg_wt):
    for k in range(len(bts)):
        print(wts[k], "P", k + 1, bts[k], end=' | ')
    print("\nAverage Waiting Time =", avg_wt)

def main():
    bts = []
    num_processes = int(input("Enter the number of processes: "))

    for i in range(num_processes):
        burst_time = int(input(f"Enter burst time for process {i + 1}: "))
        bts.append(burst_time)

    bts.sort()  # Sort the burst times in ascending order
    wts, avg_wt = avg_wt_time(bts)
    display_info(wts, bts, avg_wt)

if __name__ == "__main__":
    main()
