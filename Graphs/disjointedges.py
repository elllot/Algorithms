from collections import defaultdict, deque

def update(P, R, src, sink):
    while sink != src:
        p = P[sink]
        R[(p,sink)] -= 1
        R[(sink,p)] += 1
        sink = p

def disjoint_edges(edges, src, sink):
    G, R = defaultdict(list), {} # R: residual capacity
    for f,t in edges:
        G[f].append(t)
        G[t].append(f)
        R[(f, t)], R[(t, f)] = 1, 0 # forward and reverse edge
    found = True
    max_flow = 0
    while found:
        found = False
        queue, P, V = deque([src]), {}, set([src])
        while queue:
            v = queue.popleft()
            for vt in G.get(v, []):
                if R[(v, vt)] > 0 and vt not in V:
                    V.add(vt)
                    P[vt] = v
                    if vt == sink: 
                        found = True; break
                    queue.append(vt)
            if found: 
                max_flow += 1
                update(P, R, src, sink); break
    return max_flow

if __name__ == "__main__":
    edges = \
        [
            [0,1],[0,2],[0,3],[1,2],[2,3],
            [2,6],[3,6],[4,2],[5,1],
            [6,5],[5,4],[4,7],[5,7],[6,7]
        ]
    
    print(disjoint_edges(edges,0,7))