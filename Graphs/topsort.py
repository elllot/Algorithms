import collections
import itertools

class Node:
    def __init__(self, key):
        self.key = key
        self.edges = {} # is this the best?

def graphFromEdges(edges):
    graph = collections.defaultdict(list)
    for e in edges:
        graph[e[0]].append(e[1])
    return graph

"""
# Toplogical Sort
#
# Uses a DFS approach. Picks a vertex then fully explores
# that path while pushing vertices that have been fully visited
# onto the stack which keeps a topologically reversed order.
"""

def topper(v, visited, stack, G):
    if v in visited: return
    visited.add(v)
    if v in G:
        for vert in G[v]:
            topper(vert, visited, stack, G)
    stack.append(v)

def topSort(edges):
    G = graphFromEdges(edges)
    visited, stack = set(), []
    for v in G:
        topper(v, visited, stack, G)
    return stack[::-1]

"""
# Cycle Detection
# 
# Similar to Topological sort but keeps track of vertices that 
# are currently being visited to see if any vertices lead back to it 
# before completion of that path. Could also implement using 3 hashsets
# with an edge map given separately
"""

def cycles(v, g, G, B, parents):
    if v in B: return False
    if v in G: return True
    # has to belong to W since each vertex can only live in one group
    G.add(v) #transfer from White to Gray
    if v in g:
        for vt in g[v]:
            parents[vt] = v
            if cycles(vt, g, G, B, parents): return True
    G.remove(v); B.add(v) #transfer to Gray to Black
    del parents[v] # remove from parent map as this vertex is completed
    return False

def cycleDetection(edges):
    G, B = set(), set()
    graph = graphFromEdges(edges)
    for v in graph:
        # no need to check membership to Gray as all vertices 
        # in Gray should turn Black before DFS exits
        if v not in B: 
            # to return cycle as well
            parents = {}
            if cycles(v, graph, G, B, parents): 
                piv = itr = next(iter(parents.values()))
                res = [piv]
                while parents[itr] != piv:
                    itr = parents[itr]
                    res.append(itr)
                return True, res
    return False, None


# Testing 

edges = [['A','C'], ['B','C'], ['B','D'], ['C','E'], \
        ['D','F'],['E','F'], ['E','H'], ['F','G']]
cEdges = [[1,2],[1,3],[7,4],[4,1],[4,5],[5,6],[6,4]]
#res = topSort(edges)
res2 = cycleDetection(cEdges)
print(res2)

