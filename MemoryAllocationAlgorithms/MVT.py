def MVT(memory_size, processes):
    memory = 0 
    for index, process in enumerate(processes):
        if process < memory_size - memory: 
            memory += process
            print("Memory allocated for process P" + str(index) + " of size " + str(process))
        else:
            print("Memory Unavilable for process P" + str(index) + " of size " + str(process))
    print("\nTotal External Fragmentation : ", memory_size - memory)


if __name__ == "__main__":
    memory_size = 600
    processes = [200, 342, 100, 150, 50, 122, 134, 267, 88]
    MVT(memory_size, processes)