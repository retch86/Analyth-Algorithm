from algoritms import *
from sort import selection_sort

def testing():
    print("\nLINEAR SEARCH TEST:")
    test_func_linear(linear_search)
    print("\nBINARY SEARCH TEST:")
    test_func_binary(binary_search)

def test_func_linear(func):
    # TEST 1
    arr = []
    x = 1
    res = -1
    print("TEST 1 DONE") if func(arr, x)[0] == res else print("ERROR 1 TEST INCORRECT")

    # TEST 2
    arr = [1, 2, 3]
    x = 4
    res = -1
    print("TEST 2 DONE") if func(arr, x)[0] == res else print("ERROR 2 TEST INCORRECT")

    # TEST 3
    arr = [1, 2, 3]
    x = 1
    res = 0
    print("TEST 3 DONE") if func(arr, x)[0] == res else print("ERROR 3 TEST INCORRECT")

    # TEST 4
    arr = [1, 2, 3]
    x = 2
    res = 1
    print("TEST 4 DONE") if func(arr, x)[0] == res else print("ERROR 4 TEST INCORRECT")

    # TEST 5
    arr = [1, 2, 3]
    x = 3
    res = 2
    print("TEST 5 DONE") if func(arr, x)[0] == res else print("ERROR 5 TEST INCORRECT")

    # TEST 6
    arr = [3, 2, 1]
    x = 1
    res = 2
    print("TEST 6 DONE") if func(arr, x)[0] == res else print("ERROR 6 TEST INCORRECT")

def test_func_binary(func):
    # TEST 1
    arr = []
    x = 1
    res = -1
    print("TEST 1 DONE") if func(selection_sort(arr), x)[0] == res else print("ERROR 1 TEST INCORRECT")

    # TEST 2
    arr = [1, 2, 3]
    x = 4
    res = -1
    print("TEST 2 DONE") if func(selection_sort(arr), x)[0] == res else print("ERROR 2 TEST INCORRECT")

    # TEST 3
    arr = [1, 2, 3]
    x = 1
    res = 0
    print("TEST 3 DONE") if func(selection_sort(arr), x)[0] == res else print("ERROR 3 TEST INCORRECT")

    # TEST 4
    arr = [1, 2, 3]
    x = 2
    res = 1
    print("TEST 4 DONE") if func(selection_sort(arr), x)[0] == res else print("ERROR 4 TEST INCORRECT")

    # TEST 5
    arr = [1, 2, 3]
    x = 3
    res = 2
    print("TEST 5 DONE") if func(selection_sort(arr), x)[0] == res else print("ERROR 5 TEST INCORRECT")

    # TEST 6
    arr = [3, 2, 1]
    x = 1
    res = 0
    print("TEST 6 DONE") if func(selection_sort(arr), x)[0] == res else print("ERROR 6 TEST INCORRECT")

if __name__ == '__main__':
    testing()