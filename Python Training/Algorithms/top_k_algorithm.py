import heapq

def find_top_k_elements(nums, k):
    
    print("Initial stack is --> ", nums)
    
    # get the first 3 elements of the list
    min_heap = nums[:k]
    # sort the elements or heapify in this sense
    heapq.heapify(min_heap)
    print("Initial heap is --> ", min_heap)

    for num in nums[k:]:
        # if the next element is greater than the first element
        if num > min_heap[0]:
            # pop the first element
            heapq.heappop(min_heap)
            # add the next element
            heapq.heappush(min_heap, num)
            print(min_heap)
    # return the sorted 3 elements
    return sorted(min_heap, reverse=True)

# Example usage:
nums = [3, 1, 5, 4, 2, 7, 6]
k = 3
top_k_elements = find_top_k_elements(nums, k)
print(f"Top {k} elements:", top_k_elements)