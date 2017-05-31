import collections
import MinHeapMap as MinHeap
import DisjointSet as DS

#Minimum Spanning Trees
def makeGraph(edges):
	G, W = collections.defaultdict(list), {}
	V = [] # list of vertices. will be used for heap
	for e in edges:
		if e[0] not in G: V.append([e[0], float("inf")])
		if e[1] not in G: V.append([e[1], float("inf")])
		G[e[0]].append(e[1])
		G[e[1]].append(e[0])
		W[(e[0],e[1])] = e[2]
		W[(e[1],e[0])] = e[2]
	return G, W, V

#Prim
def prims(edges):
	G, W, V = makeGraph(edges)
	V[0][1] = 0 # start with any node
	heap = MinHeap.MinHeap(V)
	mEdges, res = {}, []
	while not heap.isEmpty():
		v, w = heap.extract_min()
		print(v, w)
		if v in mEdges: res.append(mEdges.pop(v))
		for vt in G.get(v, []):
			if heap.containsKey(vt) and heap.getValueByKey(vt) > W[(v, vt)]: 
				heap.decreaseKey(vt, W[(v, vt)]) # decrease key in heap
				mEdges[vt] = (v, vt) # indicate source 
	return res

#Kruskal
def kruskals(edges):
	edges.sort(key=lambda x: x[2]) # sort according to weight
	vertices = set()
	for e in edges:
		vertices.add(e[0])
		vertices.add(e[1])
	res, total_length = [], 0
	# creating a disjoint set of all vertices
	dj = DS.DisjointSet(list(vertices)) 
	for e in edges:
		if dj.union(e[0], e[1]):
			res.append((e[0],e[1]))
			total_length += e[2]
	return res, total_length

edges = \
	[
		['A','D',1],['A','B',3],['B','D',3],['D','C',1],
		['B','C',1],['D','E',6],['C','E',5],['C','F',4],
		['E','F',2]
	]

#print(prims(edges))
print(kruskals(edges))