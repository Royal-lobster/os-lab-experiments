# Simulate the file allocation for sequenced stratagy

import pprint
def serialized_file_allocation(disk, block_size, directory, files):
    for file_name, file_size in files:
        #### initialize required file variables ####
        file_size_to_allocate = file_size
        blocks_consumed = 0
        starting_block =  len(disk) + 1 if len(disk) != 0 else 0

        #### allocate file to disk and update dictonary ####
        while file_size_to_allocate != 0:

            #### if remaining file size is greater than block size then allocate entire block
            if file_size_to_allocate >= block_size:
                file_size_to_allocate -= block_size
                disk.append({"File Name": file_name, "Space Occupied": block_size})
                blocks_consumed += 1

            #### if remaining file size is smaller than block size then allocate acordingly
            else:
                disk.append({"File Name": file_name, "Space Occupied": file_size_to_allocate})
                file_size_to_allocate = 0
                blocks_consumed += 1
        #### update the directory entry of file ####
        directory.append({"File Name": file_name,"Starting Block":starting_block, "Size": blocks_consumed})

    #### print disk and directory to output ####
    print("Disk =>")
    pprint.pprint(disk)
    print("\nDirectory =>")
    pprint.pprint(directory)

if __name__ == "__main__":
    disk = []
    block_size = 10
    directory = []
    files = [('file-1', 40),('file-2', 34),('file-3', 22),('file-4', 38)]
    serialized_file_allocation(disk, block_size, directory, files)
