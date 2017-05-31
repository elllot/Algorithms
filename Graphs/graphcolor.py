from collections import defaultdict

def color(v, p, G, C, N, colored, cnt):
	colors = set(range(1, N+1))
	if v in G:
		for vt in G[v]:
			if C[vt] in colors: colors.remove(C[vt])
	for c in colors:
		C[v] = c
		if colored + 1 == cnt: return True
		if v in G:
			for vt in G[v]:
				if vt != p and not C[vt] and color(vt, v, G, C, N, colored + 1, cnt): 
					return True
		C[v] = None
	return False

def coloring(edges, N):
	G = defaultdict(list)
	C = {}
	for f,t in edges:
		G[f].append(t)
		G[t].append(f)
		C[t] = C[f] = None
	# assuming connected graph
	if color(list(G.keys())[0], None, G, C, N, 0, len(C)): return C
	print("Impossible")

if __name__ == "__main__":
	edges = \
		[
			[2,3],[3,4],[4,5],[5,1],
			[1,6],[2,7],[3,8],[4,9],[5,10],
			[6,8],[6,9],[7,10],[7,9],[8,10]
		]

	C = coloring(edges, 3)
	if C: print(C)