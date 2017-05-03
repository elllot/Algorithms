"""
# Heap of key,val pairs in the form of [key, val]. List was used since tuples are immutable
# Extended, with a map, to use for Dijkstra's algorithm
"""
class MinHeap: 

	def __init__(self, arr=[]):
		self.heap = arr
		self.elems = len(arr)
		self.positions = {} # map for positions
		self.build_max_heap()

	def isEmpty(self):
		return self.elems == 0
	"""
	# Helper Methods for indexing 
	"""
	def parent(self, i):
		return (i-1)//2

	def left(self, i):
		return i * 2 + 1

	def right(self, i):
		return i * 2 + 2

	"""
	# Position mapping 
	"""
	def containsKey(self, k):
		return k in self.positions

	def getPosition(self, k):
		return self.positions[k]

	def printPositions(self):
		print(self.positions)

	"""
	# Standard Heap methods
	"""
	def build_max_heap(self):
		nonleaves = (self.elems-1)//2 
		# populate map
		for i in range(self.elems):
			self.positions[self.heap[i][0]] = i
		# heapify
		for i in range(nonleaves, -1, -1):
			self.min_heapify(i)

	def getMin(self):
		return heap[0]

	def extract_min(self):
		if self.elems < 1: return None
		mn = self.heap[0]
		# swap top with last
		self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0] 
		self.positions[self.heap[0][0]] = 0
		self.elems -= 1
		# is this necessary? could optimize by reducing size only 
		# when elems is sufficiently smaller
		del self.positions[self.heap[-1][0]] # delete from position map
		self.heap.pop() 
		self.min_heapify(0)
		return mn

	def min_heapify(self, i): # top - down traversal
		l, r, mn = self.left(i), self.right(i), i
		if l < self.elems and self.heap[l][1] < self.heap[i][1]: mn = l
		if r < self.elems and self.heap[r][1] < self.heap[mn][1]: mn = r
		if mn != i:
			self.heap[i], self.heap[mn] = self.heap[mn], self.heap[i]
			# updating positions
			self.positions[self.heap[i][0]] = i
			self.positions[self.heap[mn][0]] = mn
			return self.min_heapify(mn)
		return i # i must be the min as this is the terminating condition
	
	def fix(self, i):
		p = self.parent(i)
		while i > 0 and self.heap[i][1] < self.heap[p][1]:
			self.heap[i], self.heap[p] = self.heap[p], self.heap[i]
			# updating positions
			self.positions[self.heap[i][0]] = i
			self.positions[self.heap[p][0]] = p
			i, p = p, self.parent(p)
		return i # return final index

	def decreaseKey(self, k, val):
		i = self.getPosition(k)
		if i >= self.elems: return False # out of bounds
		self.heap[i][1] = val
		return self.fix(i)

	def increaseKey(self, k, val):
		i = self.getPosition(k)
		if i >= self.elems: return False # out of bounds
		self.heap[i][1] = val
		return self.min_heapify(i) # since current node was increased, need to bubble down

	def insertKey(self, k): # space update?
		self.heap.append(k)
		self.positions[k[0]] = self.elems
		self.elems += 1
		return self.fix(self.elems-1)

	def getValueByKey(self, k):
		return self.heap[self.positions[k]][1]

	def printHeap(self):
		print(self.heap)
