from utils import *
from measure import *

TABLE_PATH = 'data/real.csv'

menu = '''Меню:
    1. Алгоритм полного перебор 
    2. Муравьиный алгоритм 
    3. Загрузить матрицу расстояний
    4. Параметризация 
    5. Замерить время 
    6. Распечатать матрицу 
    7. Результат работы алгоритмов
    8. Сгенерировать матрицу
    0. Завершить 
Выбор: '''

option = -1
while (option != 0):
    option = 0
    try:
        option = int(input(menu))
    except:
        option = -1
    if (option == 1):
        parseFullCombinations()
    elif (option == 2):
        parseAntAlg()
    elif (option == 3):
        mat = np.array(readMatrix())
        if len(mat) > 0:
            np.savetxt(TABLE_PATH , mat, delimiter=",")
        else:
            print("Введенная матрица не валидная")
    elif (option == 4):
        parametrization(type = CSV)
    elif (option == 5):
        testing()
    elif (option == 6):
        printMatrix()
    elif option == 7:
        parseAll()
    elif option == 8:
        n = int(input("Введите размер матрицы:"))
        mat = generateMatrix(n,0,100)
        np.savetxt(TABLE_PATH, mat, delimiter=",")

    else:
        print("Всего хорошего!")