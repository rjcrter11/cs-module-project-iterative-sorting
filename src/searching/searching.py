def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    if len(arr) == 0:
        return -1
    low = 0
    high = len(arr) - 1
    while low <= high:
        guess = (low + high) // 2
        if arr[guess] == target:
            return guess
        elif arr[guess] > target:
            high = guess - 1
        else:
            low = guess + 1

    return -1  # not found
