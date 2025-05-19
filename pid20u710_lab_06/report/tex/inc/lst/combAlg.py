def CombAlg(mtx, size):

    places = np.arange(size)
    placesCombinations = list()

    for combination in it.permutations(places):
        combArr = list(combination)
        placesCombinations.append(combArr)

    minLen = float("inf")

    for i in range(len(placesCombinations)):
        curLen = 0
        for j in range(size):
            startCity = placesCombinations[i][j - 1]
            endCity = placesCombinations[i][j]
            curLen += mtx[startCity][endCity]

        if (curLen < minLen):
            minLen = curLen
            bestRoute = placesCombinations[i]

    return minLen, bestRoutes