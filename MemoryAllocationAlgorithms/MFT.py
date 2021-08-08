# write a python program to simulate Memory Fixed Partitioning Scheme
import pprint

def first_come_first_serve(fixed_partitions, processes_sizes):
    
    #### initialize memory with partitions ####
    memory = []
    for partition in fixed_partitions:
        memory.append({"partition_size":partition, "allocated_process_size":None})
    
    #### initialize variables ####
    total_internal_fragmentation = 0
    total_external_fragmentation = 0
    total_partitions = len(fixed_partitions)

    #### allocate memory to processes ####
    for current_process_size in processes_sizes:
        for current_memory_partition in memory:
            #### check if memory partition is empty ####
            if current_memory_partition["allocated_process_size"] == None:
                #### check if memory block has capacity to allocate current process ####
                if  current_memory_partition["partition_size"] >= current_process_size:
                    current_memory_partition["allocated_process_size"] = current_process_size
                    total_internal_fragmentation += current_memory_partition["partition_size"] - current_process_size    
                    break
    
    #### calculate external fragmentation ####
    for current_memory_partition in memory:
        if current_memory_partition["allocated_process_size"] == None:
            total_external_fragmentation += current_memory_partition["partition_size"]

    #### print results ####
    print("\n======== First come First Serve =========")
    print("Processes size : " + str(processes_sizes))
    print("Memory =>")
    pprint.pprint(memory)
    print("Total Internal Fragmentation: " + str(total_internal_fragmentation))
    print("Total External Fragmentation: " + str(total_external_fragmentation))



def best_fit(fixed_partitions, processes_sizes):
    #### initialize memory with partitions ####
    memory = []
    for partition in fixed_partitions:
        memory.append({"partition_size":partition, "allocated_process_size":None})
    
    #### initialize variables ####
    total_internal_fragmentation = 0
    total_external_fragmentation = 0
    total_partitions = len(fixed_partitions)

    #### allocate memory to processes ####
    for current_process_size in processes_sizes:
        #### find best fit memory partition ####
        min_partition_no = None
        for partiton_no, partition in enumerate(memory):
            if partition["allocated_process_size"] == None:
                if partition["partition_size"] >= current_process_size:
                    if min_partition_no == None:
                        min_partition_no = partiton_no
                    elif memory[min_partition_no]["partition_size"] > partition["partition_size"]:
                        min_partition_no = partiton_no
        #### insert process in to found partion ####
        if min_partition_no != None:
            memory[min_partition_no]["allocated_process_size"] = current_process_size
            total_internal_fragmentation += memory[min_partition_no]["partition_size"] - current_process_size
    
    #### calculate external fragmentation ####
    for current_memory_partition in memory:
        if current_memory_partition["allocated_process_size"] == None:
            total_external_fragmentation += current_memory_partition["partition_size"]

    #### print results ####
    print("\n================ Best Fit ================")
    print("Processes size : " + str(processes_sizes))
    print("Memory =>")
    pprint.pprint(memory)
    print("Total Internal Fragmentation: " + str(total_internal_fragmentation))
    print("Total External Fragmentation: " + str(total_external_fragmentation))

def worst_fit(fixed_partitions, processes_sizes):
     #### initialize memory with partitions ####
    memory = []
    for partition in fixed_partitions:
        memory.append({"partition_size":partition, "allocated_process_size":None})
    
    #### initialize variables ####
    total_internal_fragmentation = 0
    total_external_fragmentation = 0
    total_partitions = len(fixed_partitions)

    #### allocate memory to processes ####
    for current_process_size in processes_sizes:
        #### find best fit memory partition ####
        max_partition_no = None
        for partiton_no, partition in enumerate(memory):
            if partition["allocated_process_size"] == None:
                if partition["partition_size"] >= current_process_size:
                    if max_partition_no == None:
                        max_partition_no = partiton_no
                    elif memory[max_partition_no]["partition_size"] < partition["partition_size"]:
                        max_partition_no = partiton_no
        #### insert process in to found partion ####
        if max_partition_no != None:
            memory[max_partition_no]["allocated_process_size"] = current_process_size
            total_internal_fragmentation += memory[max_partition_no]["partition_size"] - current_process_size
    
    #### calculate external fragmentation ####
    for current_memory_partition in memory:
        if current_memory_partition["allocated_process_size"] == None:
            total_external_fragmentation += current_memory_partition["partition_size"]

    #### print results ####
    print("\n================ Worst Fit ================")
    print("Processes size : " + str(processes_sizes))
    print("Memory =>")
    pprint.pprint(memory)
    print("Total Internal Fragmentation: " + str(total_internal_fragmentation))
    print("Total External Fragmentation: " + str(total_external_fragmentation))
    print("\n")


if __name__ == "__main__":
    fixed_partitions = [100, 500, 200, 300, 600]
    processes_sizes = [212, 417, 112, 426]
    first_come_first_serve(fixed_partitions, processes_sizes)
    best_fit(fixed_partitions, processes_sizes)
    worst_fit(fixed_partitions, processes_sizes)