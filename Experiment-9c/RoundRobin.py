def main():
    n = int(input("Enter the number of processes: "))
    burst_time = []
    waiting_time = [0] * n
    turnaround_time = [0] * n
    remaining_burst_time = [0] * n

    for i in range(n):
        bt = int(input(f"Enter Burst Time for process {i + 1}: "))
        burst_time.append(bt)
        remaining_burst_time[i] = bt

    time_slice = int(input("Enter the size of time slice: "))

    max_burst_time = max(burst_time)
    temp = 0
    total_waiting_time = 0
    total_turnaround_time = 0

    for j in range((max_burst_time // time_slice) + 1):
        for i in range(n):
            if remaining_burst_time[i] != 0:
                if remaining_burst_time[i] <= time_slice:
                    turnaround_time[i] = temp + remaining_burst_time[i]
                    temp += remaining_burst_time[i]
                    remaining_burst_time[i] = 0
                else:
                    remaining_burst_time[i] -= time_slice
                    temp += time_slice

    for i in range(n):
        waiting_time[i] = turnaround_time[i] - burst_time[i]
        total_turnaround_time += turnaround_time[i]
        total_waiting_time += waiting_time[i]

    print("\nThe Average Turnaround Time is --", total_turnaround_time / n)
    print("The Average Waiting Time is --", total_waiting_time / n)
    print("\n\tPROCESS\t BURST TIME \t WAITING TIME\tTURNAROUND TIME")
    for i in range(n):
        print(f"\t{i + 1} \t {burst_time[i]} \t\t {waiting_time[i]} \t\t {turnaround_time[i]}")

if __name__ == "__main__":
    main()
