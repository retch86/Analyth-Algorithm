from algoritms import linear_search, binary_search
import sys
from tests import testing
from research import research
from menu import menu
from sort import selection_sort

choice = -1
while choice != 0:
    menu()
    choice = int(input("Выберите пункт меню: "))
    if choice == 0:
        sys.exit()
    elif choice == 1:
        n = int(input("Введите размер целочисленного массива: "))
        arr = list()
        for i in range(n):
            arr.append(int(input(f'Введите {i + 1}-ый элемент массива: ')))

        while True:
            try:
                x = int(input("Введите число, которое надо найти: "))
            except ValueError:
                break

            index_linear, comparisons_linear = linear_search(arr, x)
            print("Введённый массив: ", *arr)
            if index_linear == -1:
                print(f'Заданный элемент {x} не найден линейным поиском. Выполнено {comparisons_linear} сравнений')
            else:
                print(f'Линейный поиск нашел элемент {x} на позиции {index_linear + 1} за {comparisons_linear} сравнений')

            arr_sorted = selection_sort(arr)
            index_binary, comparisons_binary = binary_search(arr_sorted, x)
            print("Искомый массив: ", *arr_sorted)
            if index_binary == -1:
                print(f'Заданный элемент {x} не найден бинарным поиском. Выполнено {comparisons_binary} сравнений')
            else:
                print(f'Бинарный поиск нашел элемент {x} на позиции {index_binary + 1} за {comparisons_binary} сравнений')
    elif choice == 2:
        research(1)
    elif choice == 3:
        research(2)
    elif choice == 4:
        research(3)
    elif choice == 5:
        testing()
