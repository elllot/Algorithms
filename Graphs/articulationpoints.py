from collections import defaultdict, deque
import random

def find_points(v, p, G, L, D, A, time):
    L[v] = D[v] = time
    mx = childs = 0
    for vt in G.get(v,[]):
        if vt != p: # important to skip parent
            if vt not in L:
                childs += 1
                find_points(vt, v, G, L, D, A, time + 1)
            # Keeping track of min of neighboring lows to update value.
            # Keeping track of max of neighboring lows to see if discover 
            # time at current node is lower than that max.
            L[v], mx = min(L[v], L[vt]), max(mx, L[vt])
    if p is None and childs > 1 or p is not None and D[v] <= mx:
        A.append(v)

def articulation_points(edges):
    G = defaultdict(list)
    for f,t in edges:
        G[f].append(t)
        G[t].append(f)
    lows, disc, a_pts = {}, {}, []
    # assuming graph is connected
    root = random.choice(list(G.keys()))
    print(root)
    find_points(root, None, G, lows, disc, a_pts, 0)
    return a_pts

if __name__ == "__main__":
    edges = \
        [
            ['C','D'],['A','C'],['B','C'],['B','A'],
            ['D','E'],['E','G'],['G','F'],['E','F'],
            ['F','H']
        ]
    print(articulation_points(edges))