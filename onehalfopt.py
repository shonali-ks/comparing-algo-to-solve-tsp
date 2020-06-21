import time


def distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1.0 / 2.0)


def build_graph(points):
    graph = {}
    for u in range(len(points)):
        for v in range(len(points)):
            if u != v:
                if u not in graph:
                    graph[u] = {}

                graph[u][v] = distance(points[u][0], points[u][1], points[v][0],
                                                        points[v][1])

    return graph


class Disjointsets:
    def __init__(self):
        self.cost = {}
        self.parents = {}

    def __getitem__(self, object):
        if object not in self.parents:
            self.parents[object] = object
            self.cost[object] = 1
            return object

        # find root
        path = [object]
        root = self.parents[object]
        while root != path[-1]:
            path.append(root)
            root = self.parents[root]

          # path compression
        for ancestor in path:
            self.parents[ancestor] = root
        return root

    def __iter__(self):
        return iter(self.parents)

    #union of set
    def union(self, *objects):
        roots = [self[x] for x in objects]
        maxcost = max([(self.cost[r], r) for r in roots])[1]
        for r in roots:
            if r != maxcost:
                self.cost[maxcost] += self.cost[r]
                self.parents[r] = maxcost


def mst(G):
    tree = []
    subtrees = Disjointsets()
    for W, u, v in sorted((G[u][v], u, v) for u in G for v in G[u]):
        if subtrees[u] != subtrees[v]:
            tree.append((u, v, W))
            subtrees.union(u, v)

    return tree


def odd_degree(MST):
    temp = {}
    vertexes = []
    for edge in MST:
        if edge[0] not in temp:
            temp[edge[0]] = 0

        if edge[1] not in temp:
            temp[edge[1]] = 0

        temp[edge[0]] += 1
        temp[edge[1]] += 1

    for vertex in temp:
        if temp[vertex] % 2 == 1:
            vertexes.append(vertex)

    return vertexes


def minimum_weight_matching(MST, G, odd_vert):
    import random
    random.shuffle(odd_vert)

    while odd_vert:
        v = odd_vert.pop()
        length = float("inf")
        u = 1
        closest = 0
        for u in odd_vert:
            if v != u and G[v][u] < length:
                length = G[v][u]
                closest = u

        MST.append((v, closest, length))
        odd_vert.remove(closest)


def eulerian_tour(MatchedMSTree, G):
    
    next_vertex = {}
    for edge in MatchedMSTree:
        if edge[0] not in next_vertex:
            next_vertex[edge[0]] = []

        if edge[1] not in next_vertex:
            next_vertex[edge[1]] = []

        next_vertex[edge[0]].append(edge[1])
        next_vertex[edge[1]].append(edge[0])

    # finds the hamiltonian circuit
    start_vertex = MatchedMSTree[0][0]
    tour_path = [next_vertex[start_vertex][0]]

    while len(MatchedMSTree) > 0:
        for i, v in enumerate(tour_path):
            if len(next_vertex[v]) > 0:
                break

        while len(next_vertex[v]) > 0:
            w = next_vertex[v][0]

            hamiltonian(MatchedMSTree, v, w)

            del next_vertex[v][(next_vertex[v].index(w))]
            del next_vertex[w][(next_vertex[w].index(v))]

            i += 1
            tour_path.insert(i, w)

            v = w

    return tour_path


def hamiltonian(MatchedMST, v1, v2):

    for i, item in enumerate(MatchedMST):
        if (item[0] == v2 and item[1] == v1) or (item[0] == v1 and item[1] == v2):
            del MatchedMST[i]

    return MatchedMST

def onehalf(data):
    # build a graph
    G = build_graph(data)
    # print("Graph: ", G)
    
    # build a minimum spanning tree
    MSTree = mst(G)
    # print("MST: ", MSTree)

    # find odd degree
    odd = odd_degree(MSTree)
    #print("Vertices having odd degree ", odd)

    # add minimum weight matching edges to MST
    minimum_weight_matching(MSTree, G, odd)
    #print("Minimum weight matching: ", MSTree)

    # find an eulerian tour
    tour = eulerian_tour(MSTree, G)
    #print("Eulerian tour: ", tour)

    current = tour[0]
    path = [current]
    visited = [False] * len(tour)
    visited[0] = True

    length = 0

    for v in tour[1:]:
        if not visited[v]:
            path.append(v)
            visited[v] = True

            length += G[current][v]
            current = v

    path.append(path[0])
    
    print("Result path: ", path)
    print("Result cost of the path: ", length)
    

    return length, path

# start = time.clock()
#check if this satifies triangular propertly later and verify it with yashs code
# onehalf([[1380, 939], [2848, 96], [3510, 1671], [457, 334], [3888, 666], [984, 965], [2721, 1482], [1286, 525],
#              [2716, 1432], [738, 1325], [1251, 1832], [2728, 1698], [3815, 169], [3683, 1533], [1247, 1945], [123, 862],
#              [1234, 1946], [252, 1240], [611, 673], [2576, 1676], [928, 1700], [53, 857], [1807, 1711], [274, 1420],
#              [2574, 946], [178, 24], [2678, 1825], [1795, 962], [3384, 1498], [3520, 1079], [1256, 61], [1424, 1728],
#              [3913, 192], [3085, 1528], [2573, 1969], [463, 1670], [3875, 598], [298, 1513], [3479, 821], [2542, 236],
#              [3955, 1743], [1323, 280], [3447, 1830], [2936, 337], [1621, 1830], [3373, 1646], [1393, 1368],
#              [3874, 1318], [938, 955], [3022, 474], [2482, 1183], [3854, 923], [376, 825], [2519, 135], [2945, 1622],
#              [953, 268], [2628, 1479], [2097, 981], [890, 1846], [2139, 1806], [2421, 1007], [2290, 1810], [1115, 1052],
#              [2588, 302], [327, 265], [241, 341], [1917, 687], [2991, 792], [2573, 599], [19, 674], [3911, 1673],
#              [872, 1559], [2863, 558], [929, 1766], [839, 620], [3893, 102], [2178, 1619], [3822, 899], [378, 1048],
#              [1178, 100], [2599, 901], [3416, 143], [2961, 1605], [611, 1384], [3113, 885], [2597, 1830], [2586, 1286],
#              [161, 906], [1429, 134], [742, 1025], [1625, 1651], [1187, 706], [1787, 1009], [22, 987], [3640, 43],
#              [3756, 882], [776, 392], [1724, 1642], [198, 1810], [3950, 1558]])
# end = time.clock()
# print("time taken: ",end - start)


# onehalf([[1, 1], [2, 5], [8, 0]])

#
def one_and_half_algo():
    onehalf([[0, 0],[3, 0],[6, 0],[0, 3],[3, 3],[6, 3],[0, 6],[3, 6],[6, 6],])

#yashs greedy data
# onehalf([[60,100],[180,200],[80,180],[140,180],[20,160],[100,160],
#     [200,160],[140,140],[40,120],[100,120],[180,100],[60,80],
#     [120,80],[180,60],[20,40],[100,40],[200,40],[20,20],[60,20],
#     [160,20]])