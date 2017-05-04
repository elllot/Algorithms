class Node:
    def __init__(self, key):
        self.key = key
        self.edges = {} # edges from this node

class Graph:
    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.edges = edges

def printMatrix(m):
    print "------------------------------"
    for r in range(len(m)):
        print ' '.join([str(i) for i in m[r]])
    print "------------------------------"

def generateMatrices(edges, V):
    v = len(V)
    d = [[float("inf") for _ in range(v)] for _ in range(v)]
    p = [['N' for _ in range(v)] for _ in range(v)]

    # initializing diagonal to all 0's
    for i in range(v):
        d[i][i] = 0

    # initialize distance and paths
    for e in edges: # 0 -> from; 1 -> to
        d[e[0]][e[1]] = e[2] # initializing shortest distance
        p[e[0]][e[1]] = e[0] # initializing source

    return d, p

def vertices(edges):
    V = set()
    for e in edges:
        V.add(e[0]); V.add(e[1])
    return V

def floydWarshallWeighted(edges):
    V = vertices(edges)
    v = len(V)
    d, p = generateMatrices(edges, V)
    # looping through
    """
    # if going through the current anchor (k) results in a 
    # shorter path, update distance and source accordingly
    # if d[i][j] > d[i][k] + d[k][j]:
    #   d[i][j] = d[i][k] + d[k][j]
    #   path[i][j] = path[k][j]
    """
    for k in range(v):
        for i in range(v):
            for j in range(v):
                if d[i][j] > d[i][k] + d[k][j]:
                    d[i][j], p[i][j]  = d[i][k] + d[k][j], p[k][j]
    
    return d, p

def shortestPath(src, dest, d, p):
    print("doom doom")

def floydWarshallUnweighted(edges):
    # Should be failry simple. Set weight of each edge to 1
    print("workin on it")

edges = [(0,3,15), (0,1,3), (1,2,-2), (0,2,6), (2,3,2), (3,0,1)]
d, p = floydWarshallWeighted(edges)
import collections
val = collections.deque([1,2,3])
some = [4,5]
val += some,
print val