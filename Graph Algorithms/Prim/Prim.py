
INF = 9999999
#liczba wierzchołków
N = 5
# macierz sąsiedztwa
G = [
    [0, 3, 0, 3, 5],
    [3, 0, 5, 1, 0],
    [0, 5, 0, 2, 0],
    [3, 1, 2, 0, 1],
    [5, 0, 0, 1, 0]
]
# G = [ [0, 2, 0, 6, 0],
#             [2, 0, 3, 8, 5],
#             [0, 3, 0, 0, 7],
#             [6, 8, 0, 0, 9],
#             [0, 5, 7, 9, 0]]


selected_node = [0, 0, 0, 0, 0]
# zmienna licząca liczbę wierzchołków
edges = 0

# wybieramy węzęł poprzez przypisanie wartośc do wybranego indeksu
selected_node[0] = True

sum = 0

print("Wierzchołki : Waga\n")
while (edges < N - 1):

    minimum = INF
    a = 0
    b = 0

    for m in range(N):
        if selected_node[m]:
            for n in range(N):
                if ((not selected_node[n]) and G[m][n]):
                    # Jeśli to nie węzeł wybrany oraz istniej krawędź
                    if minimum > G[m][n]:
                        minimum = G[m][n]
                        a = m
                        b = n

    print(str(a) + "-" + str(b) + ":" + str(G[a][b]))
    sum += int(G[a][b])
    selected_node[b] = True
    edges += 1

print(sum)