def FCFS(arrival_time, number_of_processes, burst_time):
    #### initialize clock ####
    current_clock_cycle = 0

    #### initialize required variables ####
    turn_around_time = [0] * number_of_processes
    waiting_time = [0] * number_of_processes

    #### initialize starting process as 0 ####
    current_process = 0
    remaining_processes = number_of_processes


    while remaining_processes > 0:
        #### check if arrival time of current process is reached ####
        if current_clock_cycle >= arrival_time[current_process]:
            current_clock_cycle += burst_time[current_process]
            turn_around_time[current_process] = current_clock_cycle - arrival_time[current_process]
            waiting_time[current_process] = turn_around_time[current_process] - burst_time[current_process]
            current_process += 1
            remaining_processes -= 1

        #### if no process is ready, sleep for 1 clock cycle ####
        else: 
            current_clock_cycle += 1

    #### Display processes along with all details ####
    print("Processes    Arrival Time    Burst Time     Waiting",
          "Time    Turn-Around Time")
    total_waiting_time = 0
    total_turn_around_time = 0
    for i in range(number_of_processes):
        total_waiting_time = total_waiting_time + waiting_time[i]
        total_turn_around_time = total_turn_around_time + turn_around_time[i]
        print(" ", i + 1,"\t\t",arrival_time[i], "\t\t", burst_time[i],
              "\t\t", waiting_time[i], "\t\t", turn_around_time[i])

    print("\nAverage waiting time = %.5f " % (total_waiting_time / number_of_processes))
    print("Average turn around time = %.5f " % (total_turn_around_time / number_of_processes))

if __name__ == "__main__":
    arrival_time = [0, 1, 5, 6]
    number_of_processes = 4
    burst_time = [2,2,3,4]
    FCFS(arrival_time, number_of_processes, burst_time)

