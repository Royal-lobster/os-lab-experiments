# Stimulate the FIFO Page replacement Algorithm for 
# page reference strings -
# 4, 7, 6, 1, 7, 6, 2, 7, 2, 7, 1, 4, 3, 2, 1, 6, 7, 2

if __name__ == "__main__":

    #### Initialize the page reference string ####
    reference_string = "4, 7, 6, 1, 7, 6, 2, 7, 2, 7, 1, 4, 3, 2, 1, 6, 7, 2"
   
    #### Converting the reference string to a list ####
    pages = [int(x) for x in reference_string.split(',')]

    #### Initialize the FIFO Queue ####
    queue = []
    queue_limit = 4
    page_fault_count = 0
    page_hit_count = 0

    #### Iterate to reference string and accumulate page fault count ####
    for page in pages:
        if page in queue:
            page_hit_count += 1
        else:
            if len(queue) == queue_limit:
                queue.pop(0)
            queue.append(page)
            page_fault_count += 1

    #### Print the page fault and hit counts ####
    print("[FIFO] Hits => ", page_hit_count)
    print("[FIFO] Misses => ", page_fault_count)







   
    
