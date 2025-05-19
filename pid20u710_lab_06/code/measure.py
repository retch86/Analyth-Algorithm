from utils import generateMatrix, readFileMatrix
from time import process_time
from algorithms import CombAlg, antAlg
import matplotlib.pyplot as plt

LATEX = 0
CSV = 1

def testing():
    try:
        sizeStart = int(input("\n\nВведите начальный размер матрицы: "))
        sizeEnd = int(input("Введите конечный размер матрицы: "))
        if (sizeStart > sizeEnd or sizeStart < 0 or sizeEnd < 0):
            raise Exception
    except:
        print("Неправильные размеры матрицы!")
        return
    timeFullCombinations = []
    timeAntAlg = []
    sizes = [i for i in range(sizeStart, sizeEnd + 1)]
    count = 0

    for size in sizes:
        count += 1
        mtx = generateMatrix(size, 1, 2)

        start = process_time()
        CombAlg(mtx, size)
        end = process_time()
        timeFullCombinations.append(end - start)

        start = process_time()
        antAlg(mtx, size, 0.5, 0.5, 0.5, 250)
        end = process_time()

        timeAntAlg.append(end - start)

        print(f"Прогресс: {((count / len(sizes)) * 100):3d}%")

    print("\n Размер | Время полного перебора | Время муравьиного алгоритма")
    print("-" * (8 + 1 + 24 + 1 + 29))

    for i in range(len(sizes)):
        print(f" {sizes[i]:6d} | {timeFullCombinations[i]:22.6f} | {timeAntAlg[i]:27.6f}")

    f_latex = open("latex_table.txt", "w")

    for i in range(len(sizes)):
        f_latex.write(f"%{sizes[i]:4d} & {timeFullCombinations[i]:10.6f} & {timeAntAlg[i]:10.6f} \\\\ \\hline\n")

    f_latex.close()

    fig = plt.figure(figsize=(10, 7))
    plot = fig.add_subplot()
    plot.plot(sizes, timeFullCombinations, label = "Полный перебор",marker='*')
    plot.plot(sizes, timeAntAlg, label="Муравьиный алгоритм")

    plt.legend()
    plt.grid()
    plt.title("Временные характеристики")
    plt.ylabel("Затраченное время (с)")
    plt.xlabel("Размер матрицы")

    plt.show()

def parametrization(type = CSV):
    alpha_arr = [num / 10 for num in range(1, 10,2)]
    kEva_arr = [num / 10 for num in range(1, 10,2)]
    eliteKoeff = 0.5
    eliteAnts = 2
    days_arr = [1, 5, 10, 30, 100]
    times = 10
    size = 10

    matrix1 = readFileMatrix("real.csv")
    matrix2 = readFileMatrix("gen.csv")

    optimal1 = CombAlg(matrix1, size)
    optimal2 = CombAlg(matrix2, size)

    file1 = open("parametrization_class1.txt", "w")
    file2 = open("parametrization_class2.txt", "w")

    count = 0
    countAll = len(alpha_arr) * len(kEva_arr)

    for alpha in alpha_arr:
        beta = 1 - alpha
        for kEva in kEva_arr:
            count += 1

            for days in days_arr:
                results1 = []
                results2 = []
                for _ in range(times):
                    res1 = antAlg(matrix1, size, alpha, beta, kEva, days, eliteAnts, eliteKoeff)
                    res2 = antAlg(matrix2, size, alpha, beta, kEva, days, eliteAnts, eliteKoeff)
                    results1.append(res1)
                    results2.append(res2)

                if (type == LATEX):
                    sep = " & "
                    ender = " \\\\"
                elif (type == CSV):
                    sep = ", "
                    ender = ""
                else:
                    sep = " | "
                    ender = ""
                res1 = max(results1, key = lambda x: x[0])
                res2 = max(results2, key = lambda x: x[0])
                str1 = "%4.1f%s%4.1f%s%4d%s%5d%s%5d%s\n" \
                    % (alpha, sep, kEva, sep, days, sep, optimal1[0], sep, res1[0] - optimal1[0], ender)

                str2 = "%4.1f%s%4.1f%s%4d%s%5d%s%5d%s\n" \
                    % (alpha, sep, kEva, sep, days, sep, optimal2[0], sep, res2[0] - optimal2[0], ender)

                file1.write(str1)
                file2.write(str2)

            print(f"Прогресс: {((count / countAll) * 100):3f}%")

    file1.close()
    file2.close()