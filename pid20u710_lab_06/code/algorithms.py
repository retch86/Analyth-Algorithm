import itertools as it
import numpy as np
from random import random

MIN_PHEROMONE = 0.01

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

    return minLen, bestRoute

def calculateQ(mtx, size):
    q = 0
    count = 0
    for i in range(size):
        for j in range(size):
            if (i != j):
                q += mtx[i][j]
                count += 1
    return q / count

def calculatePheromones(size):
    min_phero = 1
    pheromones = [[min_phero for i in range(size)] for j in range(size)]
    return pheromones


def calculateVisibility(mtx, size):
    visibility = [[0] * size for _ in range(size)]
    
    for i in range(size):
        for j in range(size):
            if i != j:
                visibility[i][j] = 1 / mtx[i][j]

    return visibility


def calculateVisitedPlaces(route, ants):
    visited = []
    for ant in range(ants):
        visited.append([route[ant]])
    return visited


def calculateLength(mtx, route):
    length = 0

    for routeLen in range(len(route)):
        length += mtx[route[routeLen - 1], route[routeLen]]
    
    return length


def updatePheromone(mtx, cities, visited, pheromones, q, k_evaporation, elite_ant_paths, eliteKoeff):

    for i in range(cities):
        for j in range(cities):
            dif = 0
            for ant in range(cities):
                cur_dist = calculateLength(mtx, visited[ant])
                dif += q / cur_dist
            for elitePath in elite_ant_paths:
                if (i, j) in zip(elitePath, elitePath[1:]):
                    dif += eliteKoeff

            pheromones[i][j] *= (1 - k_evaporation)
            pheromones[i][j] += dif
            if (pheromones[i][j] < MIN_PHEROMONE):
                pheromones[i][j] = MIN_PHEROMONE

    return pheromones


def findProbs(pheromones, visibility, visited, places, ant, alpha, beta):
    pk = [0] * places

    for place in range(places):
        if place not in visited[ant]:
            ant_place = visited[ant][-1]
            pk[place] = pow(pheromones[ant_place][place], alpha) * \
                pow(visibility[ant_place][place], beta)
        else:
            pk[place] = 0

    sum_pk = sum(pk)

    for place in range(places):
        pk[place] /= sum_pk

    return pk

def chooseNextСity(pk):
    posibility = random()
    choice = 0
    chosenPlace = 0
    while ((choice < posibility) and (chosenPlace < len(pk))):
        choice += pk[chosenPlace]
        chosenPlace += 1

    return chosenPlace

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