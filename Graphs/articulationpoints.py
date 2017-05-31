from collections import defaultdict
import random

def dfs(v, p, G, A, D, L, time):
    D[v] = L[v] = time
    mx = cnt = 0
    if v in G:
        if len(G[v]) == 1: return L[v] # leaf
        for vt in G[v]:
            if vt != p: # skip parent
                if vt not in L:
                    cnt += 1
                    dfs(vt, v, G, A, D, L, time + 1)
                L[v], mx = min(L[v], L[vt]), max(mx, L[vt])
    if p is not None and D[v] <= mx \
        or p is None and cnt > 1: A.append(v)
            

def tarjan(edges):
    G = defaultdict(list)
    for f,t in edges:
        G[f].append(t)
        G[t].append(f)
    A, D, L = [], {}, {}
    root = random.choice(list(G.keys()))
    dfs(root, None, G, A, D, L, 0)
    return A
        

if __name__ == "__main__":
    
    edges = \
        [
            ['A','C'],['B','C'],['C','D'],['D','E'],
            ['E','G'],['G','F'],['F','H'],['E','F'],
            ['A','B']
        ]

    """
    edges = \
        [
            [1,6],[1,0],[2,1],[0,2],[1,3],[1,4],[4,5],[3,5]
        ]
    """
    print(tarjan(edges))
