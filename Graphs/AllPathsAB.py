import collections

def makeGraph(edges):
    G = collections.defaultdict(list)
    for e in edges:
        G[e[0]].append(e[1])
    return G

def traverse(v, G, trg, visited, path, paths):
    if v in visited: return
    elif v == trg: paths.append('->'.join(path + [str(v)]))
    else:
        visited.add(v)
        path.append(str(v))
        if v in G:
            for vt in G[v]:
                traverse(vt, G, trg, visited, path, paths)
        visited.remove(v)
        path.pop()

# DAG
def allPaths(edges, src, trg):
    if src == trg: return []
    G = makeGraph(edges)
    print(G)
    visited = set()
    paths, path = [], [str(src)]
    for v in G[src]:
        traverse(v, G, trg, visited, path, paths)
    return paths

edges = \
    [
        [0,1], [1,3], [0,2], [2,0], [0,3], [2,1]
    ]

print(allPaths(edges, 2, 3))