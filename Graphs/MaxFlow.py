from collections import defaultdict, deque

def makeGraph(edges):
    G, W = defaultdict(list), defaultdict(dict)
    for e in edges:
        # adjacency lists
        G[e[0]].append(e[1])
        G[e[1]].append(e[0])
        # would need to take care of duplicate edges in case of erroneous input
        W[e[0]][e[1]] = e[2]
        W[e[1]][e[0]] = 0 # Adding backward edge
    return G, W

def find_path(queue, parents, visited, G, W, sink):
    while queue:
        v = queue.popleft()
        if v in G:
            for vt in G[v]:
                if W[v][vt] > 0: # residual capacity > 0 indicates reachability 
                    if vt not in visited:
                        parents[vt] = v
                        if vt == sink: return True
                        visited.add(vt)
                        queue.append(vt)
    return False

# helper method to find the min_flow (bottleneck) of an augmented path
def find_bottleneck(parents, sink, W):
    mn = float("inf")
    while sink in parents:
        mn = min(mn, W[parents[sink]][sink])
        sink = parents[sink]
    return mn

# updating residual capacity for edges
# subtract min_flow from forward edges and add the same to reverse edges
def update_capacity(parents, sink, W):
    mn = find_bottleneck(parents, sink, W)
    while sink in parents:
        W[parents[sink]][sink] -= mn # decrementing residual capacity for path
        W[sink][parents[sink]] += mn # adding to reverse edges
        sink = parents[sink]
    return mn

# using Ford-Fulkerson's Algorithm for max flow (Edmonds Karp's implementation)
def ford_fulkerson(edges, src, sink):
    G, W = makeGraph(edges)
    max_flow = 0
    while True:
        queue = deque()
        parents = {}
        visited = set([src])
        for v in G[src]:
            if W[src][v] > 0: 
                parents[v] = src
                visited.add(v)
                queue.append(v)
        if not find_path(queue, parents, visited, G, W, sink): break
        max_flow += update_capacity(parents, sink, W)
    return max_flow

if __name__ == "__main__":
    edges = \
        [
            ['A','B',3],['A','D',3],['C','A',3],['B','C',4],
            ['C','E',2],['E','B',1],['C','D',1],['D','E',2],
            ['D','F',6],['F','G',9],['E','G',1]
        ]

    print(ford_fulkerson(edges, 'A', 'G'))
