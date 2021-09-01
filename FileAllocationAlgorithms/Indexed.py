def indexed_file_allocation(disk, block_size, directory, files):
    for file_name, file_size in files:
        pass

if __name__ == "__main__":
    disk = []
    block_size = 10
    directory = []
    files = [('file-1', 40),('file-2', 34),('file-3', 22),('file-4', 38)]
    indexed_file_allocation(disk, block_size, directory, files)