import collections
import MinHeap
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
		if v in G:
			for vt in G[v]:
				if heap.containsKey(vt) and heap.getValueByKey(vt) > W[(v, vt)]: 
					heap.decreaseKey(vt, W[(v, vt)]) # decrease key in heap
					mEdges[vt] = (v, vt) # indicate source 
	return res

#Kruskal
def kruskals(edges):
	return 



edges = \
	[
		['A','D',1],['A','B',3],['B','D',3],['D','C',1],
		['B','C',1],['D','E',6],['C','E',5],['C','F',4],
		['E','F',2]
	]

print(prims(edges))