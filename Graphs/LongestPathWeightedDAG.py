import collections
"""
# Longest Path in a directed graph(tree)
#
# Using Top sort 
"""

# generate directed graph(tree)
def makeDAG(edges):
	graph, weights, maxes = collections.defaultdict(set), {}, {}
	for e in edges:
		graph[e[0]].add(e[1])
		weights[(e[0],e[1])] = e[2]
		maxes.setdefault(e[0], float("-inf"))
		maxes.setdefault(e[1], float("-inf"))
	return graph, weights, maxes

def TShelper(v, D, G, order):
	if v in D: return
	# add cycle detection here if we aren't guaranteed an Acyclical DAG
	# if v in V: handle cycle
	if v in G: #DFS to explore all before 
		for vt in G[v]:
			TShelper(vt, D, G, order)
	D.add(v)
	order.appendleft(v) # add to front as we'll be adding terminal vertices first

def topSort(G):
	D = set() # done set. Add visiting set if not guaranteed an Acyclical DAG
	order = collections.deque()
	for v in G:
		TShelper(v, D, G, order)
	return order

# iterative top sort using a stack
def topSortIter(G):
	return 

def longestPathDAGTopSort(edges):
	G, W, M = makeDAG(edges)
	order = topSort(G)
	mx = float("-inf")
	print(W)
	print(order)
	while order:
		v = order.popleft()
		M[v] = max(M[v], 0)
		mx = max(mx, M[v])
		for vt in G[v]:
			M[vt] = max(M[vt], M[v] + W[(v, vt)])
	print(M)
	return mx

"""
# Longest Path in a directed graph(tree)
#
# Keeping list of references
"""

# generate directed graph(tree)
def makeDAG_ref(edges):
	graph, weights = collections.defaultdict(set), {}
	for e in edges:
		graph[e[0]].add(e[1])
		weights[(e[0],e[1])] = e[2]
	return graph, weights

# Longest path in a weighted directed tree
def longestPathDAG(edges):
	G, W = makeDAG(edges)
	queue = collections.deque()
	maxes = {}
	# grab all leaves and add to queue
	for g in G:
		if len(G[g]) == 1: queue.append(g)
		maxes[g] = [0, 0]
	maxPath = 0
	while queue:
		v = queue.popleft()
		# grabbing local maxima
		maxPath = max(maxPath, maxes[v][0] + maxes[v][1])
		vertices = G.pop(v)
		#if vertices:

edges2 = \
	[
		[0,1,5], [0,2,3],
		[1,3,6], [1,2,2],
		[2,4,4], [2,5,2], [2,3,7],
		[3,5,1], [3,4,-1],
		[4,5,-2]
	]

print(longestPathDAGTopSort(edges2))