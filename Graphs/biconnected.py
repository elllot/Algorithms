from collections import defaultdict
import random

def tarjan(v, p, time, L, D, G):
	D[v] = L[v] = time 
	if v not in G: return False # in case of a disconnected node
	mx = childs = 0
	for vt in G[v]:
		if vt != p:
			if vt not in L:
				childs += 1
				if not tarjan(vt, v, time + 1, L, D, G): return False
			L[v], mx = min(L[v], L[vt]), max(mx, L[vt])
	if p is None and childs > 1 \
		or p is not None and D[v] <= mx: return False # articulation point found
	return True

def biconnected(edges, N):
	G = defaultdict(list)
	for f,t in edges:
		G[f].append(t)
		G[t].append(f)
	low, discovered = {}, {}
	root = random.choice(list(G.keys())) # grab random node as start
	return tarjan(root, None, 0, low, discovered, G) and len(low) == N

if __name__ == "__main__":
	edges = \
		[
			[1,0],[0,3],[2,0],[2,4],[1,2],[3,4]
		]
	print(biconnected(edges, 5))

