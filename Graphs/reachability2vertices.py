from collections import defaultdict

def reachable(edges, src, trg):
	G = defaultdict(list)
	for f,t in edges:
		G[f].append(t)
	stack = [src]
	visited = set([src])
	while stack:
		v = stack.pop()
		visited.add(v)
		for vt in G.get(v, []):
			if vt == trg: return True
			if vt not in visited:
				visited.add(vt)
				stack.append(vt)
	return False

if __name__ == "__main__":
	edges = \
		[
			[0,2],[2,0],[0,1],[1,2],
			[2,3],[3,3]
		]
	print(reachable(edges, 3, 0))