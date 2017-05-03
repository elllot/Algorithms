class BinaryIndexTree:
    def __init__(self):
        self.elems = []
        self.tree = []
    
    def populate(self, arr):
        if not arr: return
        self.elems = arr
        self.generateTree()

    def getParent(self, val):
        return val - (val & -val)
    
    def getNext(self, val):
        return val + (val & -val)

    def generateTree(self):
        self.tree = [0] * (len(self.elems)+1)
        for i,v in enumerate(self.elems):
            self.updateTree(i,v)
            # a for loop
    
    def modify(self, index, val):
        temp = val - self.elems[index]
        self.elems[index] = val
        self.updateTree(index, temp)

    def updateTree(self, index, val):
        i = index + 1
        while i < len(self.tree):
            self.tree[i] += val
            i = self.getNext(i)
        print("tree after inserting index:", index, " val:", val, ";", self.tree)
    
    def getSum(self, index):
        i, _sum = index + 1, 0
        while i > 0:
            _sum += self.tree[i]
            i = self.getParent(i)
        return _sum

    def prefixSum(self, end, start=0):
        if start < 0 or start > len(self.elems) or end < 0 or end > len(self.elems): return 0
        if start == 0: return self.getSum(end)
        else: return self.getSum(end) - self.getSum(start-1)

BIT = BinaryIndexTree()
BIT.populate([3,2,-1,6,5,4,-3,3,7,2,3])
print(BIT.tree)
print(BIT.prefixSum(5))
print(BIT.prefixSum(5,1))
