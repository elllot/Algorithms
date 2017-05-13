from collections import defaultdict

def makeGraph(edges):
	G = defaultdict(list)
	for e in edges:
		G[e[0]].append(e[1])
	return G

def traverse(v, G, elements, visited):
	if v in visited: return
	visited.add(v)
	if v in G:
		for vt in G[v]:
			traverse(vt, G, elements, visited)
	elements.append(v)

def kosaraju(edges):
	G = makeGraph(edges)
	elements = [] # stack of finished elems
	visited = set() # hashset of visited vertices
	# first pass
	for v in G:
		traverse(v, G, elements, visited)

	# reverse edges
	for e in edges:
		e[0], e[1] = e[1], e[0]

	G = makeGraph(edges)
	visited = set()
	SCC = []
	while elements:
		v = elements.pop()
		if v not in visited:
			group = []
			traverse(v, G, group, visited)
			SCC.append(group)
	return SCC

if __name__ == "__main__":

	edges = \
		[
			['A','B'],['C','A'],['B','C'],['B','D'],
			['D','E'],['E','F'],['F','D'],
			['J','K'],['I','J'],['H','I'],['G','H'],
			['J','G'],
			['G','F']
		]

	print(kosaraju(edges))