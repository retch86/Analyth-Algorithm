import matplotlib.pyplot as plt
from algoritms import *
import random
from sort import selection_sort

# X/8 + ((X >> 2) % 10 == 0 ? X % 1000: ((X >> 2) % 10 * (X % 10) + (X >> 1) % 10)
# X = 8355
LEN_X = 1091

def research(choice):
    arr = random.sample(range(10000), LEN_X)
    linear_arr_comps = [0] * LEN_X
    for i in range(LEN_X):
        linear_arr_comps[i] = linear_search(arr, arr[i])[1]

    arr_selection_sort = selection_sort(arr)
    binary_sort_arr_comps = [0] * LEN_X
    for i in range(LEN_X):
        binary_sort_arr_comps[i] = binary_search(arr_selection_sort, arr[i])[1]


    fig = plt.subplots(figsize=(8, 4))
    plt.xlabel("Позиция элементов в массиве")
    plt.ylabel("Количество сравнений")
    if choice == 1:
        plt.bar([i for i in range(LEN_X)], linear_arr_comps)
    elif choice == 2:
        plt.bar([i for i in range(LEN_X)], binary_sort_arr_comps)
    elif choice == 3:
        plt.bar([i for i in range(LEN_X)], selection_sort(binary_sort_arr_comps))
    plt.show()


if __name__ == '__main__':
    research()