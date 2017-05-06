import collections

# Implementation without a separate node class

# Disjoint set with rank & path compression
class DisjointSet:
    def __init__(self, arr):
        self.ranks = {}
        self.parents = {}
        self.makeSet(arr)

    # initialize all elements to a singleton 
    def makeSet(self, arr):
        for a in arr:
            self.parents[a] = a
            self.ranks[a] = 0
    
    # returns the rep of a value
    def findSet(self, v):
        # path compression
        if self.parents[v] == v: return v
        self.parents[v] = self.findSet(self.parents[v])
        return self.parents[v]

    def union(self, u, v):
        # check if both u and v exists
        if v not in self.parents or u not in self.parents: return None
        U, V = self.findSet(u), self.findSet(v)
        # if either does not exist or both are in the same set
        if not U or not V or U == V: return False
        if self.ranks[V] > self.ranks[U]: # since u has the higher rank, merge v to u
            self.parents[u] = V
        else: # merge u to v
            if self.ranks[U] == self.ranks[V]: self.ranks[U] += 1 # increment if two are the same
            self.parents[v] = U
        return True
    
    def showRanks(self):
        print(self.ranks)
    
    def showParents(self):
        print(self.parents)

    def showAll(self):
        print(self.ranks)
        print(self.parents)

arr = ['a','b','c','d','e','f','g']
dj = DisjointSet(arr)
dj.union('a', 'b')
dj.union('b', 'c')
dj.union('c', 'e')
dj.union('g', 'e')
dj.union('d', 'f')
dj.showRanks()
dj.showParents()
