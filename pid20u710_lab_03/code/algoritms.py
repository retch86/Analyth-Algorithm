def linear_search(arr, x):
    if len(arr) == 0:
        return -1, 0

    comparisons = 0
    for index, i in enumerate(arr):
        comparisons += 1
        if i == x:
            return index, comparisons

    return -1, comparisons

def binary_search(arr, x):
    if len(arr) == 0:
        return -1, 0

    comparisons = 0
    left = 0
    right = len(arr) - 1

    while left <= right:
        comparisons += 1
        middle = (left + right) // 2

        if arr[middle] == x:
            return middle, comparisons
        elif arr[middle] < x:
            left = middle + 1
        else:
            right = middle - 1

    return -1, comparisons
