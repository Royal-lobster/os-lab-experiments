def ResourceRequest(Process, Request, Available, Allocation, Max):
    number_of_process = len(Max)
    number_of_resources = len(Available)

    #### create need matrix ####
    Need = []
    for x in range(number_of_process):
        currentProcessNeed = [0] * number_of_resources
        for y in range(number_of_resources):
            currentProcessNeed[y] = Max[x][y] - Allocation[x][y]
        Need.append(currentProcessNeed)
    
    #### check if request is less than available resources ####
    resource_check = [False] * number_of_resources
    for x in range(number_of_resources):
        if Request[x] > Available[x]:
            resource_check[x] = True
    if True in resource_check:
        print("ERROR: Request is Greater Than Available Resources")
        return

    #### check if request is greater than need ####
    need_check = [False] * number_of_resources
    for x in range(number_of_resources):
        if Request[x] > Need[Process][x]:
            need_check[x] = True
    if True in need_check:
        print("ERROR: Request is Greater Than Informed Needs")
        return

    #### Assume the request is granted and check the safety of the system ####
    for x in range(number_of_resources):
        Available[x] = Available[x] - Request[x]
        Allocation[Process][x] = Allocation[Process][x] + Request[x]
        Need[Process][x] = Need[Process][x] - Request[x]
    safetyAlgorithm(Available, Allocation, Max, Need, number_of_process, number_of_resources) 
    

def safetyAlgorithm(Available, Allocation, Max, Need, number_of_process, number_of_resources):
    #### Initialize ####
    Work = Available
    Finish = [False] * number_of_process
    SafeSequence = []

    remaining_rounds = 3
    while remaining_rounds > 0:
        remaining_rounds -= 1
        for current_process in range(number_of_process):
            #### check if the need is safe ####
            is_process_need_safe = True
            for current_resource in range(number_of_resources):
                if Need[current_process][current_resource] > Work[current_resource] and is_process_need_safe:
                    is_process_need_safe = False 
                if not is_process_need_safe: break

            #### check if the allocation for this round is safe and then allocate ####
            if Finish[current_process] == False and is_process_need_safe:
                for current_resources in range(number_of_resources):
                    Work[current_resources] = Work[current_resources] + Allocation[current_process][current_resources]
                Finish[current_process] = True
                SafeSequence.append(current_process)

        #### check if all processes is true then break ####
        if Finish == [True] * number_of_process:
                print("System is safe to grant the request")
                print("The safe sequence is: ", SafeSequence)
                break
        
if __name__ == "__main__":
    Available = [3, 3, 2]
    Allocation = [[0, 1, 0],[2, 0, 0], [3, 0, 2],[2, 1, 1], [0, 0, 2]]
    Max = [[7, 5, 3],[3, 2, 2], [9, 0, 2],[2, 2, 2], [4, 3, 3]]
    Request = [1, 0, 2]
    ResourceRequest(1, Request, Available, Allocation, Max)
