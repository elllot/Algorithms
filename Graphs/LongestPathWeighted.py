import collections

"""
# Longest Path in an undirected graph(tree)
#
"""

# generate undirected graph(tree)
def makeGraph(edges):
	graph, weights = collections.defaultdict(set), {}
	for e in edges:
		graph[e[0]].add(e[1])
		graph[e[1]].add(e[0])
		weights[(e[0],e[1])] = e[2]
		weights[(e[1],e[0])] = e[2]
	return graph, weights

# Longest path in a weighted undirected tree
def longestPath(edges):
	G, W = makeGraph(edges)
	queue = collections.deque()
	maxes = {}
	for g in G:
		if len(G[g]) == 1: queue.append(g)
		maxes[g] = [0, 0]
	maxPath = 0
	while queue:
		v = queue.popleft()
		# grabbing local maxima
		maxPath = max(maxPath, sum(maxes[v]))
		# should only have 1 outdegree as these are all leaves
		vertices = G.pop(v)
		if vertices: # if last node, skip
			nxt = vertices.pop() # remove vertex from graph
			G[nxt].remove(v) # remove edge 
			l1 = max(maxes[v]) + W[(v, nxt)]
			# keep max 2 paths leading into the vertex
			maxes[nxt] = sorted(maxes[nxt] + [l1], reverse=True)[:2]
			# if the vertex at the end of the relaxed edge is a leaf, add to queue
			if len(G[nxt]) == 1: queue.append(nxt)
	return maxPath


edges = \
	[
		[1,2,3],[2,3,4],[2,6,2],[6,4,6],[6,5,5]
	]

print(longestPath(edges))


