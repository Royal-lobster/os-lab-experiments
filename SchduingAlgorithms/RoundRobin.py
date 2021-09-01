def round_robbin(arrival_time, number_of_processes, burst_time, time_quantum):

    #### initialize two queues for round robbin ####
    current_clock_cycle = 0
    ready_queue = []

    #### initialize required variables ####
    turn_around_time = [0] * number_of_processes
    waiting_time = [0] * number_of_processes

    #### initialize remaining_time with burst_time ####
    remaining_time = [burst_time[i] for i in range(number_of_processes)]

    #### initialize starting process as 0 ####
    current_process = 0

    while True:
        #### check new processes and append to the ready queue ####
        for pID in range(number_of_processes):
            if current_clock_cycle >= arrival_time[pID] and remaining_time[pID] != 0:
                if pID not in ready_queue and pID != current_process:
                    ready_queue.append(pID)

        #### append previous current process to the end of the ready queue ####
        if remaining_time[current_process] != 0: ready_queue.append(current_process) 

        #### get first process from the ready queue to current process ####
        current_process = ready_queue.pop(0) 
                    
        #### check if arrival time of current process is reached ####
        if current_clock_cycle >= arrival_time[current_process]:
            if remaining_time[current_process] > time_quantum:
                current_clock_cycle += time_quantum
                remaining_time[current_process] -= time_quantum
            else:
                current_clock_cycle = current_clock_cycle + remaining_time[current_process]
                turn_around_time[current_process] = current_clock_cycle - arrival_time[current_process]
                waiting_time[current_process] = turn_around_time[current_process] - burst_time[current_process]
                remaining_time[current_process] = 0

        #### if no process is ready, sleep for 1 clock cycle ####
        else:
            current_clock_cycle += 1
        
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

if __name__ == "__main__":
    arrival_time = [0,1, 2, 3, 4]
    number_of_processes = 5
    burst_time = [5,3,1,2,3]
    time_quantum = 2
    round_robbin(arrival_time, number_of_processes, burst_time, time_quantum)
