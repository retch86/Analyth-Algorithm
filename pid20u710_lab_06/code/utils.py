import numpy as np
from os import system
from random import randint
from algorithms import CombAlg, antAlg

def generateMatrix(size, randStart, randEnd):
    mtx = np.zeros((size, size), dtype = int)

    for i in range(size):
        for j in range(size):
            if (i == j):
                num = 0
            else:
                num = randint(randStart, randEnd)
            mtx[i][j] = num
            mtx[j][i] = num

    half = size // 2
    for i in range(1, half):
        for j in range(1, half):
            mtx[size - i][size - j] = mtx[i][j]

    return mtx

def readFileMatrix(filename):
    filePath = "data/" + filename
    mat = np.loadtxt(open(filePath, "rb"), delimiter=",", skiprows=0)
    return mat

def listDataFiles():
    system("ls ./data > files.txt") 
    f_files = open("files.txt", "r")
    files = f_files.read().split()
    f_files.close()

    print("\nФайлы: ",)
    for i in range(len(files)):
        print("%d. %s" % (i + 1, files[i]))

    return files

def printMatrix():
    files = listDataFiles()
    try:
        fileIndex = int(input("\nВыберите файл: ")) - 1
    except:
        print("Неверно выбран файл\n")
        return
    mtx = readFileMatrix(files[fileIndex])
    for i in range(len(mtx)):
        for j in range(len(mtx[0])):
            print(f"{mtx[i][j]:.1f}", end = " ")
        print()

def readMatrixFile():
    files = listDataFiles()
    fileIndex = int(input("\nВыберите файл: ")) - 1
    mtx = readFileMatrix(files[fileIndex])
    return mtx

def parseFullCombinations():
    mtx = readMatrixFile()
    size = len(mtx)
    result = CombAlg(mtx, size)
    print("\nМинимальная сумма пути = ", result[0],
            "\nПуть: ", result[1])

def readKoeffs():
    try:
        alpha = float(input("\n\nВведите коэффициент alpha: " ))
        beta = 1 - alpha
        k_evaporation = float(input("Введите коэффициент evaporation: " ))
        days = int(input("Введите кол-во дней: " ))
        eliteAnts = int(input('Введите количество элитных муравьев: '))
        eliteKoeff = float(input('Введите коэффициент усиления феромонов элитных муравьев: '))
    except:
        print("Неверный ввод!")
        alpha = 0
        beta = 1
        k_evaporation = 0.5
        days = 10
        eliteAnts = 2
        eliteKoeff = 1.0

    return alpha, beta, k_evaporation, days, eliteAnts, eliteKoeff

def parseAntAlg():
    mtx = readMatrixFile()
    size = len(mtx)
    alpha, beta, k_evaporation, days, eliteAnts, eliteKoeff = readKoeffs()
    result = antAlg(mtx, size, alpha, beta, k_evaporation, days, eliteAnts, eliteKoeff)
    print("\nМинимальная сумма пути = ", result[0],
            "\nПуть: ", result[1])

def parseAll():
    mtx = readMatrixFile()
    size = len(mtx)
    alpha, beta, k_evaporation, days, eliteAnts, eliteKoeff = readKoeffs()

    result = CombAlg(mtx, size)

    print("\nПолный перебор \
            \nМинимальная длина пути = ", result[0],
            "\nПуть: ", result[1])

    result = antAlg(mtx, size, alpha, beta, k_evaporation, days, eliteAnts, eliteKoeff)

    print("\nМуравьиный алгоритм \
            \nМинимальная длина пути = ", result[0],
            "\nПуть: ", result[1])

def isFloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def checkFloatMatrix(mtx):
    for row in mtx:
        for val in row:
            if not isFloat(val):
                return False
    return True

def readMatrix():
    mtx = []
    try:
        while True:
            row = input("Введите элементы матрицы через пробел или нажмите Enter для окончания ввода:")
            if not row:
                break
            row_values = row.split()
            if not checkFloatMatrix([row_values]):
                print("Ошибка: Неверное значение!")
                return []
            mtx.append([float(val) for val in row_values])
    except EOFError:
        pass
    if len(mtx) != len(mtx[0]):
        return []
    return mtx