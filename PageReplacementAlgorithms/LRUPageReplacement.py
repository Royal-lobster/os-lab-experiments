# Stimulate the LRU Page replacement Algorithm for 
# page reference strings -
# 4, 7, 6, 1, 7, 6, 2, 7, 2, 7, 1, 4, 3, 2, 1, 6, 7, 2

if __name__ == "__main__":

    #### Initialize the page reference string ####
    reference_string = "4, 7, 6, 1, 7, 6, 2, 7, 2, 7, 1, 4, 3, 2, 1, 6, 7, 2"
   
    #### Converting the reference string to a list ####
    pages = [int(x) for x in reference_string.split(',')]

    #### Initialize the FIFO memory ####
    memory = []
    memory_limit = 3
    page_fault_count = 0
    page_hit_count = 0

    #### create an array for count of page references ####
    recently_used_count = dict()

    #### Iterate to reference string and accumulate page fault count ####
    for index, page in enumerate(pages):
        #### If page is already in memory, then increment the recently used count ####
        if page in memory:
            recently_used_count[page] = index
            page_hit_count += 1

        #### If page is not in memory (IN CASE OF PAGE FAULT) ####
        else:            
            #### If memory is full, then remove the LRU page from the memory and in counter ####
            if len(memory) == memory_limit:
                least_recently_used_page = min(recently_used_count, key=recently_used_count.get)
                memory.remove(least_recently_used_page)
                del recently_used_count[least_recently_used_page]

            #### add page to memory and update the recently used count ####
            memory.append(page)
            recently_used_count[page] = index
            page_fault_count += 1

    #### Print the page fault and hit counts ####
    print("[LRU] Hits => ", page_hit_count)
    print("[LRU] Misses => ", page_fault_count)



