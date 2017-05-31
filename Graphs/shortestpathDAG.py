from collections import defaultdict, deque

def top_sort(v, G, V, order):
	if v in V: return
	V.add(v)
	for vt in G.get(v, []):
		top_sort(vt, G, V, order)
	order.appendleft(v)

def shortest_path(edges, src):
	G = defaultdict(list)
	D = {}
	W = {}
	for f,t,w in edges:
		G[f].append(t)
		W[(f, t)] = w
		D[f] = D[t] = float("inf")
	order = deque()
	V = set()
	for v in G:
		top_sort(v, G, V, order)
	D[src] = 0
	for v in order:
		for vt in G.get(v, []):
			new_dist = D[v] + W[(v, vt)]
			if new_dist < D[vt]:
				D[vt] = new_dist
	print(D)

if __name__ == "__main__":
	edges = \
		[
			['s','x',6],['s','t',2],['r','s',5],['r','t',3],
			['t','x',7],['t','z',2],['x','y',-1],['t','y',4],
			['y','z',-2],['x','z',1] 
		]
	shortest_path(edges, 's')