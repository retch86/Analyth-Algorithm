def linear_search(arr, x):
    if len(arr) == 0:
        return -1, 0
    comparisons = 0
    for index, i in enumerate(arr):
        comparisons += 1
        if i == x:
            return index + 1, comparisons
    return -1, comparisons