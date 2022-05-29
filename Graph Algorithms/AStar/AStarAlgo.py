# A star Algorhitm

adjMatrix = [[0, 5, 0, 1, 0, 0, 0, 0],
             [0, 0, 2, 0, 1, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 3],
             [0, 0, 0, 0, 1, 2, 0, 0],
             [0, 0, 4, 0, 0, 0, 0, 0],
             [4, 0, 0, 0, 0, 0, 2, 0],
             [0, 0, 0, 0, 1, 0, 0, 1],
             [0, 0, 0, 0, 2, 0, 0, 0]
             ]

heuristicValueTable = [4, 8, 3, 4, 5, 2, 1, 0]


def AStar(adjMatrix, heuristic, startNode, endNode):
    # poprzedniki
    pred = [-1] * len(adjMatrix)
    pred[startNode] = -1

    # "nieskończoność"
    inf = 999

    # szacowany koszt dostania się z s do celu
    h = heuristic

    # droga do węzła pośredniego v
    g = [inf] * len(adjMatrix)
    g[startNode] = 0

    f = [inf] * len(adjMatrix)

    # węzły "otwarte"
    S = []

    # węzły "zamknięte"
    Q = []

    v = startNode
    f[v] = g[v] + h[v]
    Q.append(v)

    while v != endNode:

        if v == 0:
            S.append(Q.pop(0))
        else:
            S.append(Q.pop(-1))

        neigbourIndexes = []
        for u in range(len(adjMatrix)):
            if adjMatrix[v][u] != 0:
                neigbourIndexes.append(u)
                if u not in S and u not in Q:
                    Q.append(u)
                    pred[u] = v
                    g[u] = adjMatrix[v][u] + g[pred[u]]
                    f[u] = h[u] + g[u]

                else:
                    g_temp = adjMatrix[v][u]
                    if g_temp < g[u]:
                        g[u] = g_temp + g[pred[u]]
                        f[u] = g[u] + h[u]


        f_temp = []
        for n in range(len(neigbourIndexes)):
            h_temp = h[neigbourIndexes[n]]
            g_temp = adjMatrix[v][neigbourIndexes[n]] + g[pred[neigbourIndexes[n]]]

            f_temp.append([h_temp + g_temp, neigbourIndexes[n]])

        f_temp.sort()

        v = f_temp[0][1]

    print("h(v) " + str(h))
    print("g(v) " + str(g))
    print("f(v) " + str(f))
    print("pred " + str(pred))

    print("\n")

    print("Droga " + str(startNode+1) + " -> " + str(endNode+1) + " = " + str(g[endNode]))
    # przebieg drogi
    droga = [endNode+1]
    k = endNode
    while g[k] != startNode:
        droga.append(pred[k]+1)
        k = pred[k]
    droga.reverse()
    print("Kolejne wierzchołki: " + str(droga))


# print(Vertexes(adjMatrix))
AStar(adjMatrix, heuristicValueTable, 0, 7)
input()