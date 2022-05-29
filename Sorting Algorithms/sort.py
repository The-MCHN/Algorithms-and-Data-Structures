import datetime
import random
# tablica do testów

# T = [0.4, -11.2, 20.1, 100, -102, -69.69]
# T = [9, 1, 2, 4, 5, 7, 8, 6, 3]


def generateList(size):
    T=[]
    for i in range(0,size):
        T.append(random.randint(-1000, 1000))
    return T

# Bubblesort

def bubbleSort(T):
    for k in range(len(T)):
        for i in range(len(T) - 1):
            if T[i] > T[i + 1]:
                h = T[i]
                T[i] = T[i + 1]
                T[i + 1] = h


# Insertsort

def insertSort(T):
    for k in range(1, len(T)):
        tmp = T[k]
        l = k - 1
        while l >= 0 and T[l] > tmp:
            T[l + 1] = T[l]
            l -= 1
        T[l + 1] = tmp

# Quicksort
# l i r to kolejno indexy lewy i prawy koniec listy
def qsort(T, l, r):

    if l >= r:
        return

    i, j = l, r
    pivot = T[r]

    while i <= j:
        while T[i] < pivot:
            i += 1
        while T[j] > pivot:
            j -= 1

        if i <= j:
            T[i], T[j] = T[j], T[i]
            i, j = i + 1, j - 1
    qsort(T, l, j)
    qsort(T, i, r)

# Mergesort

def mergeSort(T):
    if len(T) > 1:
        p = len(T) // 2
        L = T[:p]
        P = T[p:]

        mergeSort(L)
        mergeSort(P)

        i = j = k = 0

        while i < len(L) and j < len(P):
            if L[i] < P[j]:
                T[k] = L[i]
                i += 1
            else:
                T[k] = P[j]
                j += 1
            k += 1

        while i < len(L):
            T[k] = L[i]
            i += 1
            k += 1

        while j < len(P):
            T[k] = P[j]
            j += 1
            k += 1

# Heapsort
def heapify(T, n, i):
    max = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and T[max] < T[l]:
        max = l


    if r < n and T[max] < T[r]:
        max = r

    if max != i:
        T[i], T[max] = T[max], T[i]

        heapify(T, n, max)

def heapSort(T):
    n = len(T)

    for i in range(n//2 - 1, -1, -1):
        heapify(T, n, i)

    for i in range(n-1, 0, -1):
        T[i], T[0] = T[0], T[i]
        heapify(T, i, 0)



T = generateList(100)
print(T)

start_time = datetime.datetime.now()
heapSort(T)
end_time = datetime.datetime.now()

time_diff = (end_time - start_time)
execution_time = time_diff.total_seconds() * 1000
print(execution_time)
# milliseconds =
# print(milliseconds)
input()