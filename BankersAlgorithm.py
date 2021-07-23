def ResourceRequest(Process, Request, Available, Allocation, Max):
    number_of_process = len(Max)
    number_of_resources = len(Available)

    #### create need matrix ####
    Need = [[0] * number_of_resources] * number_of_process
    for x in range(number_of_process):
        for y in range(number_of_resources):
            Need[x][y] = Max[x][y] - Allocation[x][y]

    #### check if request is greater than need ####
    if Request > Need[Process]:
        print("ERROR: Request is Greater Than Informed Needs")
        return
    
    #### check if request is less than available resources ####
    if Request > Available:
        print("ERROR: Request is Greater Than Available Resources")
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
    SafeSequence = [0] * number_of_process

    for i in range(number_of_process):
        if Finish[i] == False and Need[i] <= Work:
            Work = Work + Allocation[i]
            Finish[i] = True
            SafeSequence.append(i)
        else:
            if Finish == [True] * number_of_process:
                print("System is safe to grant the request")
                print("The safe sequence is: ", SafeSequence)
                return True
            elif(Need[i] >= Work) : print("System is not safe to grant the request")


if __name__ == "__main__":
    Available = [3, 3, 2]
    Allocation = [[0, 1, 0],[2, 0, 0], [3, 0, 2],[2, 1, 1], [0, 0, 2]]
    Max = [[7, 5, 3],[3, 2, 2], [9, 0, 2],[2, 2, 2], [4, 3, 3]]
    Request = [1, 0, 2]
    ResourceRequest(0, Request, Available, Allocation, Max)
