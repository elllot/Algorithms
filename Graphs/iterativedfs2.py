from collections import defaultdict
import random

def iterative_dfs(edges, src = None):
	G = defaultdict(list)
	for f,t in edges:
		G[f].append(t)
	root = src if src is not None else random.choice(list(G.keys()))
	stack, order = [root], []
	visited = set([root])
	while stack:
		v = stack.pop()
		order.append(v)
		for vt in G.get(v, []):
			if vt not in visited:
				visited.add(vt)
				stack.append(vt)
	return order

if __name__ == "__main__":
	edges = \
		[
			[0,2],[2,1],[1,0],[0,3],[3,4],[4,0]
		]

	print(iterative_dfs(edges))