from collections import deque

class TreeNode:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None

class BSTBuilder:
    def __init__(self):
        # do something maybe?
        self.INT_MAX = float("inf")
        self.INT_MIN = -float("inf")
    
    def buildFromPreorder(self, arr):
        # preorder
        if not arr: return None
        return self.preBuilder(deque(arr), self.INT_MIN, self.INT_MAX)
    
    # DFS Builder O(n)
    def preBuilder(self, arr, _min, _max):
        if not arr: return 
        if arr[0] < _min or arr[0] > _max: return 
        root = TreeNode(arr.popleft())
        root.left = self.preBuilder(arr,_min,root.val)
        root.right = self.preBuilder(arr,root.val,_max)
        return root

    def buildFromPostorder(self, arr):
        # postorder
        if not arr: return None
        return self.postBuilder(arr, self.INT_MIN, self.INT_MAX)
    
    # DFS Builder O(n)
    def postBuilder(self, arr, _min, _max):
        if not arr: return 
        if arr[-1] < _min or arr[-1] > _max: return 
        root = TreeNode(arr.pop())
        root.right = self.postBuilder(arr,root.val,_max)
        root.left = self.postBuilder(arr,_min,root.val)
        return root

class BTreeUtil:
    def __init__(self, root=None):
        self.root = root
    
    def preHelper(self, node, _list):
        if not node: return
        _list.append(node.val)
        self.preHelper(node.left,_list)
        self.preHelper(node.right,_list)
        
    def getPreorder(self, root=None):
        rList = []
        if not root: self.preHelper(self.root, rList)
        else: self.preHelper(root, rList)
        return rList

    def postHelper(self, node, _list):
        if not node: return
        self.postHelper(node.left,_list)
        self.postHelper(node.right,_list)
        _list.append(node.val)

    def getPostorder(self, root=None):
        rList = []
        if not root: self.postHelper(self.root, rList)
        else: self.postHelper(root, rList)
        return rList

builder = BSTBuilder()
util = BTreeUtil()
root = builder.buildFromPreorder([15,9,6,3,1,5,8,13,12,25,20,16,23,29,30])
rootPost = builder.buildFromPostorder([1,5,3,8,6,12,13,9,16,23,20,30,29,25,15])
print(util.getPreorder(root))
print(util.getPostorder(rootPost))