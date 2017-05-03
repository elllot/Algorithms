import sys
class TreeNode:
    def __init__(self):
        self.val = None
        self.left = None
        self.right = None
    # look into overloading constructors

    def _print(self):
        print(self.val)
    """
    def __init__(self, v):
        self.val = v
        self.left, self.right = None, None
    def __init__(self, v, l, r):
        self.val = v
        self.left, self.right = l, r
    """ 
class NodeBased(object):
    arr = []
    head = None

    def setArray(self, arr):
        self.arr = arr

    def minVal(self, i, j):
        #print("i: %i  j: %i" % (i, j))
        node = TreeNode()
        if i == j: 
            node.val = self.arr[i]
            return node
        mid = (i + j) / 2
        node.left = self.minVal(i, mid)
        node.right = self.minVal(mid+1, j)
        node.val = min(node.left.val, node.right.val)
        return node

    def generateTree(self, arr):
        self.setArray(arr)
        self.head = self.minVal(0, len(self.arr)-1)

    def minRecursion(self, i, j, a, b, node):
        #print("i: %i, j: %i, a: %i, b: %i" % (i,j,a,b))
        if (i == a and j == b) or a == b: return node.val
        if j < a or i > b: return sys.maxint
        mid = (a + b) / 2
        return min(self.minRecursion(i, j, a, mid, node.left), self.minRecursion(i, j, mid+1, b, node.right))

    def findMin(self, i, j):
        if i < 0 or j >= len(self.arr):
            print("Recheck Index values!")
            return None
        return self.minRecursion(i, j, 0, len(self.arr)-1, self.head)
    # Inorder traversal for tree
    def inorderR(self, node):
        if not node: return
        self.inorderR(node.left)
        print(node.val)
        self.inorderR(node.right)

    def inorderTraversal(self):
        inorderR(self.head)

_list = [int(i) for i in raw_input().split()]
n = NodeBased()
n.generateTree(_list)
print(n.findMin(1, 3))
