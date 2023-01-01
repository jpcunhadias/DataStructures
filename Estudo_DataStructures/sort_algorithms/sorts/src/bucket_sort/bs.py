def bucket_sort(arr, num_buckets):
    """
    :param arr: array to be sorted
    :param num_buckets: number of buckets
    :return: sorted array
    """
   
    # Create a list of empty buckets
    buckets = [[] for _ in range(num_buckets)]

    # Distribute the elements of the input list into the buckets
    for x in arr:
        bucket_idx = int(num_buckets * x)
        buckets[bucket_idx].append(x)

    # Sort the elements within each bucket
    for bucket in buckets:
        bucket.sort()

    # Concatenate the sorted buckets to get the sorted list
    sorted_arr = [x for bucket in buckets for x in bucket]

    return sorted_arr
