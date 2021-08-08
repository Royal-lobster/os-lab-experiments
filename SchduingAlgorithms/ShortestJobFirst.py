
def SJF(arrival_time, number_of_processes, burst_time):
    #### initialize clock ####
    current_clock_cycle = 0

    #### initialize required variables ####
    turn_around_time = [0] * number_of_processes
    waiting_time = [0] * number_of_processes

    #### initialize remaining_time with burst_time ####
    remaining_time = [0] * number_of_processes
    for pID in range(number_of_processes): remaining_time[pID] = burst_time[pID]

    #### initialize starting process as 0 ####
    current_process = 0

    while True:
        #### check new processes appeared and assign current process ####
        for pID in range(number_of_processes):
            if remaining_time[pID] != 0:
                if remaining_time[current_process] == 0: current_process = pID
                if current_clock_cycle >= arrival_time[pID]:
                    if remaining_time[current_process] > remaining_time[pID] or remaining_time[current_process] == 0:
                        current_process = pID

        #### check if arrival time of current process is reached ####
        if current_clock_cycle >= arrival_time[current_process]: 
            current_clock_cycle += 1
            remaining_time[current_process] -= 1
            if remaining_time[current_process] == 0:
                turn_around_time[current_process] = current_clock_cycle - arrival_time[current_process]
                waiting_time[current_process] = turn_around_time[current_process] - burst_time[current_process]
        else: current_clock_cycle +=1

        #### end timeline if all processes are done ####
        if remaining_time == [0] * number_of_processes:
            break

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

if(__name__ == "__main__"):
    arrival_time = [0, 1, 2, 4]
    number_of_processes = 4
    burst_time = [5, 3 , 4 , 1 ]
    SJF(arrival_time, number_of_processes, burst_time)
