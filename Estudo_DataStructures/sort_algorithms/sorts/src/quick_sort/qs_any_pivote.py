def quick_sort(arr, start, end):
    if start < end:
        # Choose pivot_idx as the index of the pivot element
        pivot_idx = start

        # Partition the list around the pivot element
        pivot_idx = partition(arr, start, end, pivot_idx)

        # Recursively sort the two partitions
        quick_sort(arr, start, pivot_idx - 1)
        quick_sort(arr, pivot_idx + 1, end)

def partition(arr, start, end, pivot_idx):
    
    
    # Choose the pivot element
    pivot = arr[pivot_idx]

    # Swap the pivot element with the last element in the list
    arr[pivot_idx], arr[end] = arr[end], arr[pivot_idx]

    # Initialize the partition index
    partition_idx = start

    # Iterate through the list and partition it around the pivot element
    for i in range(start, end):
        if arr[i] < pivot:
            arr[i], arr[partition_idx] = arr[partition_idx], arr[i]
            partition_idx += 1

    # Swap the pivot element with the element at the partition index
    arr[partition_idx], arr[end] = arr[end], arr[partition_idx]

    return partition_idx

