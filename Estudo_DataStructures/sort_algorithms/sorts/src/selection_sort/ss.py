def selection_sort(arr):
    for i in range(len(arr)):
        # Find the minimum element in the unsorted portion of the list
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        
        # Swap the minimum element with the first element of the unsorted portion
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr
