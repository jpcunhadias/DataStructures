def counting_sort(arr, max_value):
  # Create a count array to store the count of each unique object
  count = [0] * (max_value + 1)

  # Loop through the input array and count the occurrences of each element
  for i in range(len(arr)):
    count[arr[i]] += 1

  # Set the index to 0
  index = 0

  # Loop through the count array and place the element in the input array
  for i in range(max_value + 1):
    for j in range(count[i]):
      arr[index] = i
      index += 1

# Test the implementation
arr = [5, 2, 4, 6, 1, 3]
counting_sort(arr, max(arr))
print(arr)  # Output: [1, 2, 3, 4, 5, 6]
