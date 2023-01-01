def radix_sort(arr):
    
    
    # Find the maximum number of digits in the list
    max_digits = max([len(str(x)) for x in arr])

    #Perform the radix sort on each digit
    for i in range(max_digits):
        buckets = [[] for _ in range(10)]
        for x in arr:
            digit = (x // 10**i) % 10
            buckets[digit].append(x)
        arr = [x for bucket in buckets for x in bucket]
    
    return arr


# Driver Code
if __name__ == '__main__':
    
    arr_test = [123, 456, 789, 321, 654, 987]
    
    print(radix_sort(arr_test))