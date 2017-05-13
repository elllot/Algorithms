from collections import defaultdict

def makeGraph(edges):
    G = defaultdict(list)
    for e in edges:
        G[e[0]].append(e[1])
        G[e[1]].append(e[0])
    return G

# check if an undirected graph is a bipartite
def checkBipartite(edges):
    colors = {}
    G = makeGraph(edges)
    for v in G:
        if v not in colors:
            stack = [(v, True)]
            while stack:
                vt, c = stack.pop()
                if vt in colors: 
                    if colors[vt] != c: return False # not a bipartite
                else:
                    colors[vt] = c
                    if vt in G:
                        for _v in G[vt]:
                            stack.append((_v, not c))
    return True


if __name__ == "__main__":
    edges = \
        [
            ['A','B'], ['B','C'],['C','D'],['G','D'],
            ['E','F'], ['H','E'],['I','H'],['B','I'],['H','F']
        ]
    print(checkBipartite(edges))