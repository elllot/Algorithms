from collections import defaultdict, deque

def makeGraph(edges):
    graph = defaultdict(set)
    for e in edges:
        graph[e[0]].add(e[1])
        graph[e[1]].add(e[0])
    return graph

def BFS(G, start):
    queue = deque([(start,0)])  
    visited = set()  
    V, farthest = None, 0
    # find farthest vertex from the arbitrary vertex
    while queue:
        v, dist = queue.popleft() 
        if dist > farthest: V, farthest = v, dist 
        visited.add(v)
        for vtx in G[v]:
            # skip if already visited. Since we're doing a BFS and there aren't any cycles,
            # we can ensure our earlier arrival at this vertex is the longer path
            if vtx not in visited: queue.append((vtx, dist+1))
    return V

# Since each vertex can be reached through a unique path in a tree (due to no cycles)
# we can keep a parent mapping to trail back to get the longest path
def BFSParent(G, start):
    parents, visited = {}, set()
    V, farthest = None, 0
    queue = deque([(start ,0, V)]) 
    # find farthest vertex from starting vertext
    while queue:
        v, dist, p = queue.popleft() 
        if dist > farthest: V, farthest = v, dist 
        visited.add(v)
        parents[v] = p
        for vtx in G[v]:
            # skip if already visited. Since we're doing a BFS and there aren't any cycles,
            # we can ensure our earlier arrival at this vertex is the longer path
            if vtx not in visited: queue.append((vtx, dist+1, v))
    return V, parents

def getLongestPath(edges):
    if not edges: return []
    G = makeGraph(edges)
    # find longest path from given vertex
    end, parents = BFSParent(G, BFS(G, G.keys()[0]))
    path = []
    while end:
        path.append(end)
        end = parents[end]
    return path, len(path) # path and length of longest path

edges = \
[
    [5,4], [4,2], [2,3], [9,2], [2,1], 
    [1,0], [1,6], [6,8], [6,7] 
]
print getLongestPath(edges)
