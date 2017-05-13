from collections import defaultdict
import DisjointSet as DS

def makeGraph(edges):
	G = defaultdict(list)
	for e in edges:
		G[e[0]].append(e[1])
		G[e[1]].append(e[0])
	return G

# DFS approach
def findCycleDFS(edges):
	if not edges: return False
	G = makeGraph(edges)
	vertices, edges = set(), set()
	for v in G:
		if v not in vertices:
			stack, cycle = [v], [v]
			while stack:
				_v = stack.pop()
				if _v in vertices: return cycle
				vertices.add(_v)
				# since undirected each connected vertex will have at least one outdegree
				for vt in G[_v]:
					if (_v, vt) not in edges:
						# indicate use for both directions
						edges.add((_v, vt))
						edges.add((vt, _v))
						stack.append(vt)
						cycle.append(vt)
	return False

if __name__ == "__main__":
	
	edges = \
		[
			['A','B'], ['B','D'],['A','C'],['C','E'],['E','D']
		]

	print(findCycleDFS(edges))