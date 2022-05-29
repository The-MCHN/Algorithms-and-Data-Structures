# # # Algorytm Dijsktry
# #

adjMatrix = [[0, 3, 0, 3, 5],
             [3, 0, 5, 2, 0],
             [0, 5, 0, 1, 0],
             [3, 1, 2, 0, 1],
             [5, 0, 0, 1, 0]]

M2 = [[0, 3, 0, 0, 3, 0],
      [0, 0, 1, 0, 0, 0],
      [0, 0, 0, 3, 0, 1],
      [0, 3, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 2],
      [6, 0, 0, 1, 0, 0]
      ]


def DijkstraAlgorithm(adjMatrix, startNode, endNode):
    INF = 9999999999
    dist = len(adjMatrix) * [INF]
    pred = len(adjMatrix) * [0]

    dist[startNode] = 0
    pred[startNode] = -1
    Q = []
    for x in range(len(adjMatrix)):
        Q.append(x)
    # Q = [0, 1, 2, 3, 4]
    S = []

    # warunek zmieniony względem pseudokodu z wykładu, ponieważ uniemożliwia dalsze wykonywanie pętli for
    while len(Q) != len(S):
        for v in range(len(adjMatrix)):

            S.append(Q[v])

            for i in range(0, len(Q)):
                if adjMatrix[v][i] != 0:
                    d = dist[v] + adjMatrix[v][i]
                    if d <= dist[i]:
                        dist[i] = d
                        pred[i] = v
    print("S " + str(S))
    print("dist " + str(dist))
    print("pred " + str(pred))

# wypisujemy przebieg

    k = endNode
    t = [S[k]]
    k = S[endNode]

    while pred[k] != -1:
        k = pred[k]

        t.append(k)

    t.reverse()
    print("Przebieg drogi od " + str(startNode) + " do " + str(endNode) + " " + str(t))
    print("Waga drogi wynosi: "+ str(dist[endNode]))





DijkstraAlgorithm(adjMatrix, 0, 4)
print("\n")
DijkstraAlgorithm(M2, 0, 5)
