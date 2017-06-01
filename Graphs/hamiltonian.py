from collections import defaultdict
import random

def find_cycle(start, v, G, V, N, cycle):
    if v == start and len(cycle) == N: 
        cycle.append(v)
        return True # terminating condition
    if v not in V:
        V.add(v)
        cycle.append(v)
        for vt in G.get(v,[]):
            if find_cycle(start, vt, G, V, N, cycle): return True
        V.remove(v) # remove from visited
        cycle.pop()
    return False

def hamiltonian_cycle(edges, N):
    G = defaultdict(list)
    for f,t in edges:
        G[f].append(t)
        G[t].append(f)
    start = random.choice(list(G.keys()))
    cycle = []
    if find_cycle(start, start, G, set(), N, cycle): return cycle
    print("NO CYCLE")

def find_path(v, G, V, N, path):
    if v not in V:
        V.add(v)
        path.append(v)
        if len(path) == N: return True
        for vt in G.get(v,[]):
            if find_path(vt, G, V, N, path): return True
        V.remove(v)
        path.pop()
    return False

def hamiltonian_path(edges, N):
    G = defaultdict(list)
    for f,t in edges:
        G[f].append(t)
        G[t].append(f)
    start = random.choice(list(G.keys()))
    path = []
    if find_path(start, G, set(), N, path): return path
    print("NO PATH")

if __name__ == "__main__":
    edges = \
        [
            [0,1],[1,2],[2,4],[1,4],[1,3],[0,3]
        ]
    
    print(hamiltonian_cycle(edges, 5))
    print(hamiltonian_path(edges, 5))