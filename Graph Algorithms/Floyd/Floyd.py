# Implementacja Algorytmu Floyda-Warshalla

# liczba wierzchołków
V = 7


INF = 99999


def floydWarshall(graph, p, start, end):
    dist = graph
    p1 = p
    # środkowy wierzchołek
    for k in range(V):
        # lewo
        for i in range(V):
            # prawo
            for j in range(V):

                if dist[i][k] + dist[k][j] < dist[i][j]:
                    p1[i][j] = p[k][j]
                    dist[i][j] = dist[i][k] + dist[k][j]
                # dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    printSolution(dist)
    print()
    printSolution(p1)

    # wyznaczanie drogi z wierzchołka start do wierzchołka end
    droga = []
    droga.append(end)
    prev = p[start - 1][end - 1]

    while droga[-1] != start:
        droga.append(prev)
        prev = p[start - 1][prev - 1]
    droga.reverse()
    print(droga)


def printSolution(dist):
    for i in range(V):
        for j in range(V):
            if (dist[i][j] == INF):
                print("I", end=" ")
            else:
                print(dist[i][j], end=" ")
            if j == V - 1:
                print("")

# macierz d_0
graph = [
    [0, 1, 5, INF, INF, INF, INF],
    [INF, 0, 2, INF, INF, INF, INF],
    [INF, INF, 0, INF, INF, INF, INF],
    [7, INF, INF, 0, 1, INF, INF],
    [INF, INF, INF, INF, 0, 1, INF],
    [2, INF, INF, 4, INF, 0, INF],
    [6, INF, INF, INF, INF, 3, INF],
]
# macierz p_0, która jest również macierzą grafu

p = [[0, 1, 1, 0, 0, 0, 0],
     [0, 0, 2, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0],
     [4, 0, 0, 0, 4, 0, 0],
     [0, 0, 0, 0, 0, 5, 0],
     [6, 0, 0, 6, 0, 0, 0],
     [7, 0, 0, 0, 0, 7, 0]
     ]

floydWarshall(graph, p, 7, 3)
