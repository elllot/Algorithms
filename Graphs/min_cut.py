from collections import defaultdict, deque

def get_min(P, R, src, sink):
	mn = float("inf")
	while sink != src:
		mn, sink = min(mn, R[(P[sink], sink)]), P[sink]
	return mn

def update_residuals(P, R, src, sink):
	m = get_min(P, R, src, sink)
	while src != sink:
		p = P[sink]
		R[(p, sink)] -= m
		R[(sink, p)] += m
		sink = p
	return m
	
def max_flow(edges, src, sink):
	G = defaultdict(list)
	R = {}
	O = defaultdict(list)
	for f,t,w in edges:
		G[f].append(t)
		# keeping track of original graph to filter out backedges
		# when identifying min cut edges
		O[f].append(t) 
		G[t].append(f)
		R[(f, t)] = w
		R.setdefault((t, f), 0)
	flow = 0
	Found = True
	while Found:
		Found = False
		P, V = {}, set([src])
		queue = deque([src])
		while queue:
			v = queue.popleft()
			for vt in G.get(v,[]):
				if R[(v, vt)] > 0 and vt not in V:
					V.add(vt)
					P[vt] = v
					queue.append(vt)
					if vt == sink:
						Found = True; break
			if Found:
				flow += update_residuals(P, R, src, sink)
				break
	min_cut = []
	queue = deque([src])
	V = set([src])
	while queue:
		v = queue.popleft()
		for vt in G.get(v,[]):
			if R[(v, vt)] == 0 and vt in O[v]: 
				min_cut.append((v, vt, R[(vt, v)])) # add back edge since it'll contain the capacity
			elif R[(v, vt)] > 0 and vt not in V:
				V.add(vt)
				queue.append(vt)
	return min_cut

if __name__ == "__main__":
	edges = \
		[
			[0,1,16],[0,2,13],[1,2,10],[2,1,4],
			[1,3,12],[2,4,14],[3,2,9],[4,3,7],
			[4,5,4],[3,5,20]
		]

	edges2 = \
		[
			['s','a',10],['s','b',8],['s','d',5],
			['b','d',3],['b','a',3],['b','c',10],
			['d','c',3],['c','t',8],['a','t',5],
			['d','t',10],['a','c',3]
		]

	#print(max_flow(edges, 0, 5))
	print(max_flow(edges2, 's','t'))
	