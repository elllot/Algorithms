import collections
import pprint

# DAG
def makeGraph(edges):
    G, V = collections.defaultdict(list), set()
    for e in edges:
        G[e[0]].append(e[1])
        V.add(e[0])
        V.add(e[1])
    return G, V

def traverse(v, G, order, M, stack, visited):
    if v in visited: 
        if stack:
            for vt in stack:
                for i in M[order[v]]: # check connecting nodes from this node
                    if i == 1: M[order[vt]][order[v]] = 1
    else:       
        if stack: 
            for vt in stack: # adding current node to all nodes in the current stack
                M[order[vt]][order[v]] = 1 # update matrix
        stack.append(v)
        visited.add(v) # add to visited as this node should be fully processed by the end of the loop below
        if v in G: # if vertex has any out degree
            for vt in G[v]:
                traverse(vt, G, order, M, stack, visited)
        stack.pop()

def transitiveClosure(edges):
    # the way I'm generating the list of vertices will leave out 
    # vertices that have 0 in & out degrees
    G, V = makeGraph(edges)
    M = [[int(i==j) for i in range(len(V))] for j in range(len(V))] # Closure matrix
    order = {}
    val = 0
    for v in V: # generating order in case vertices do not start from 0 or are not ints.
        order[v] = val; val += 1
    for v in V:
        traverse(v, G, order, M, [], set())
    return M

edges = \
    [
        [0,2],[2,0],[0,1],[1,2],[2,3]
    ]
pprint.pprint(transitiveClosure(edges))