import MinHeapMap as MinHeap
import collections

"""
# Helper method for initializing setup
#
"""
def fill(edges, weights, distances, src):
    # weights & distances
    for e in edges:    
        weights[(e[0], e[1])] = e[2]
        if e[0] != src: distances[e[0]] = float("inf") 
        if e[1] != src: distances[e[1]] = float("inf")

def fillD(edges, neighbors, weights, distances, src): # marks path both ways
    for e in edges:    
        neighbors[e[0]].append(e[1])
        neighbors[e[1]].append(e[0])
        weights[(e[0], e[1])] = e[2]
        weights[(e[1], e[0])] = e[2]
        distances[e[0]] = float("inf") if e[0] != src else 0
        distances[e[1]] = float("inf") if e[1] != src else 0

# -------------------------------------------------------------------------------------------------------

"""
# Bellman-Ford 
#
# - Time complexity: O(VE) - visits all edges E, V-1 times.
# - Space complexity: O(V) - stores distance to each V
# - Can extend to get paths to all in O(V^2 * E) which can get slower than Floyd Warshall's O(V^3)
# - Need to run the loop V-1 times due to the fact that in the worst case,
#   it will take V-1 loops to fully discover (relax) the path to a certain vertex.
#   This is due to the algorithm only updating routes that have been "discovered"
# - Detect negative weight cycles
"""
def bellmanFord(edges, src):
    weights, distances, parents = {}, {src:0}, {}
    fill(edges, weights, distances, src)
    # main loop
    for i in range(len(distances)-1):
        for w in weights:
            if distances[w[1]] > distances[w[0]] + weights[w]:
                distances[w[1]] = distances[w[0]] + weights[w]
                parents[w[1]] = w[0] # parent map incase we want the actual path
            
    # detecting negative cycles
    nCycle = False
    for w in weights:
        if distances[w[1]] > distances[w[0]] + weights[w]: nCycle = True; break

    # return shortest path and also whether there is a negative cycle or not
    return distances, parents, nCycle

# testing BellmanFord
"""
# form of [u,v,weight]
edges = [[0,2,5],[0,1,4],[1,2,-3],[2,4,4],[0,3,8],[3,4,2],[4,3,1]]
d, p, neg = bellmanFord(edges, 0)
print(d, p, neg)
"""

# -------------------------------------------------------------------------------------------------------

"""
# Defining __lt__ to augment heapq
"""

"""
# Dijkstra
#
# Min Heap + Hashmap
#
# Hashmap to keep track of existence. 
"""
def dijkstra(edges, src):
    weights, neighbors, distances = {}, collections.defaultdict(list), {src:0}
    fillD(edges, neighbors, weights, distances, src) 
    P, temp = {src:None}, []
    for k,v in distances.items():
        temp += [k, v],
    #print(temp)
    M = MinHeap.MinHeap(temp)
    #prev = None
    while not M.isEmpty():
        vertex = M.extract_min()
        distances[vertex[0]] = vertex[1]
        #P[vertex[0]], prev = prev, vertex[0]
        # checking if we've found a shorter path to each neightbor relative to the current vertex
        for v in neighbors[vertex[0]]: 
            if not M.containsKey(v): continue
            if M.getValueByKey(v) > vertex[1] + weights[(vertex[0], v)]:
                M.decreaseKey(v, vertex[1] + weights[(vertex[0], v)])
                P[v] = vertex[0]
    print(distances)
    print(P)
    return distances, P

# form of [u,v,weight]
edges = [['A','E',2],['A','B',5],['A','D',9] \
        ,['E','F',3],['B','C',2],['F','D',2],['C','D',3]]

dijkstra(edges, 'A')