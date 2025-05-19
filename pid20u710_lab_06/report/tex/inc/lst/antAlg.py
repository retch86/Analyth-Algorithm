def antAlg(mtx, cities, alpha, beta, k_evaporation, days, eliteAnts, eliteKoeff):
    q = calculateQ(mtx, cities)
    bestRoute = []
    minLen = float("inf")
    pheromones = calculatePheromones(cities)
    visibility = calculateVisibility(mtx, cities)
    
    elite_ant_paths = []
    elite_paths_updated = False

    for _ in range(days):
        route = np.arange(cities)
        visited = calculateVisitedPlaces(route, cities)

        for ant in range(cities):
            while (len(visited[ant]) != cities):
                pk = findProbs(pheromones, visibility, visited, cities, ant, alpha, beta)
                chosenPlace = chooseNextСity(pk)
                visited[ant].append(chosenPlace - 1)

            curLength = calculateLength(mtx, visited[ant])

            if (curLength < minLen):
                minLen = curLength
                bestRoute = visited[ant]
            
            if ant < eliteAnts and not elite_paths_updated:
                for elitePath in elite_ant_paths:
                    for i in range(len(elitePath) - 1):
                        pheromones[elitePath[i]][elitePath[i + 1]] *= (1 + eliteKoeff)
                elite_paths_updated = True

        pheromones = updatePheromone(mtx, cities, visited, pheromones, q, k_evaporation, elite_ant_paths, eliteKoeff)

    return minLen, bestRoute