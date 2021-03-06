# Stimulate the Optimal Page replacement Algorithm for 
# page reference strings -
# 4, 7, 6, 1, 7, 6, 2, 7, 2, 7, 1, 4, 3, 2, 1, 6, 7, 2

if __name__ == "__main__":

    #### Initialize the page reference string ####
    reference_string = "4, 7, 6, 1, 7, 6, 2, 7, 2, 7, 1, 4, 3, 2, 1, 6, 7, 2"
   
    #### Converting the reference string to a list ####
    pages = [int(x) for x in reference_string.split(',')]

    #### Initialize the FIFO memory ####
    memory = []
    memory_limit = 4
    page_fault_count = 0
    page_hit_count = 0

    #### Iterate to reference string and accumulate page fault count ####
    for index, page in enumerate(pages):
        #### If page is already in memory, then continue ####
        if page in memory:
            page_hit_count += 1

        #### If page is not in memory (IN CASE OF PAGE FAULT) ####
        else:            
            #### If memory is full, then remove the LRU page from the memory and in counter ####
            if len(memory) == memory_limit:
                ordered_future_pages = []
                #### Iterate through the memory and append the future page to the list ####
                for future_page in pages[index+1 : len(pages)]:
                    if len(ordered_future_pages) == len(memory): break
                    if future_page in memory and future_page not in ordered_future_pages:
                        ordered_future_pages.append(future_page)

                #### Remove the LRU page from the memory and in counter ####
                if len(ordered_future_pages) < len(memory):
                    redundant_pages = [x for x in memory if x not in ordered_future_pages]
                    ordered_future_pages = ordered_future_pages + redundant_pages
                    
                memory.remove(ordered_future_pages[-1])


            #### add page to memory and update the recently used count ####
            memory.append(page)
            page_fault_count += 1

    #### Print the page fault and hit counts ####
    print("[Optimal] Hits => ", page_hit_count)
    print("[Optimal] Misses => ", page_fault_count)



