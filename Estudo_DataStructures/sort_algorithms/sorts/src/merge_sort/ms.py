def merge_sort(arr):
    
    if len(arr) > 1:
        # Divide the list into two halves
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        # Recursively sort the two halves
        merge_sort(left)
        merge_sort(right)

        # Merge the sorted halves back together
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # Copy any remaining elements from the left and right halves
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    return arr
