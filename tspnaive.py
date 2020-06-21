

from sys import maxsize
V = 4


def tsp(graph, s):

    vertex = []
    for i in range(V):
        if i != s:
            vertex.append(i)  # all vertex except source

    min_path = maxsize

    while True:

        current_pathweight = 0

        k = s  # compute path weight
        for i in range(len(vertex)):
            current_pathweight += graph[k][vertex[i]]
            k = vertex[i]
        current_pathweight += graph[k][s]

        min_path = min(min_path, current_pathweight)

        if not next_permutation(vertex):
            break

    return min_path


def next_permutation(L):

    n = len(L)

    i = n - 2
    while i >= 0 and L[i] >= L[i + 1]:
        i -= 1

    if i == -1:
        return False

    j = i + 1
    while j < n and L[j] > L[i]:
        j += 1
    j -= 1

    L[i], L[j] = L[j], L[i]

    left = i + 1
    right = n - 1

    while left < right:
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1

    return True


def naive():

    graph = [[ 0,10, 8, 9, 7, 3,  5, 6, 9 ],
			[10, 0,10, 5, 6, 3 , 2, 1, 9 ],
			[ 8,10, 0, 8, 9 , 7, 3, 7, 2 ],
			[ 9, 5, 8, 0, 6 , 2, 5, 8, 4],
			[ 7, 6, 9, 6, 0, 5, 7, 3, 2],
			[ 3, 3, 7, 2, 5, 0, 2, 3, 4],
			[ 5, 2, 3, 5, 7, 2, 0, 3,4 ],
			[ 6, 1, 7, 8, 3, 3, 4, 0, 1 ],
			[ 9, 9, 2, 4, 2, 4, 4, 1, 0],]
    s = 0
    print(tsp(graph, s))
