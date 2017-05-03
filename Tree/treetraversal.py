from collections import deque
class TreeNode:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None

def inorderItr(root):
    if not root: return[]
    rList, stack = [], []
    while True:
        while root:
            stack.append(root)
            root = root.left
        if not stack: return rList
        node = stack.pop()
        rList.append(node.val)
        root = node.right

def preorderItr(root):
    if not root: return []
    rList, stack = [], [root]
    while stack:
        node = stack.pop()
        rList.append(node.val)
        if node.right: stack.append(node.right)
        if node.left: stack.append(node.left)
    return rList

def bstFromInord(arr, i, j):
    if j < i: return
    if i == j: return TreeNode(arr[i])
    mid = i+(j-i)//2
    root = TreeNode(arr[mid])
    root.left = bstFromInord(arr,i,mid-1)
    root.right = bstFromInord(arr,mid+1,j)
    return root

def preHelper(queue, mn, mx):
    if not queue or queue[0] < mn or queue[0] > mx: return
    node = TreeNode(queue.popleft())
    node.left = preHelper(queue, mn, node.val)
    node.right = preHelper(queue, node.val, mx)
    return node

def preToBST(arr):
    if not arr: return
    queue = deque(arr)
    return preHelper(queue, -float("inf"), float("inf"))

"""
root = bstFromInord([1,2,3,4,5,6,7,8,9,10], 0, 9)
print(inorderItr(root))
preOrd = preorderItr(root)
root2 = preToBST(preOrd)
print(inorderItr(root2))
"""
def lca(root, p, q):
    if root in (None, p, q): return root
    left = lca(root.left, p, q)
    right = lca(root.right, p, q)
    print("node:",root.val)
    if left: print("left:", left.val)
    if right: print("right:", right.val)
    print("-------------------------")
    return root if left and right else left or right
"""
root = TreeNode(10)
root.left = TreeNode(5)
root.left.left = TreeNode(-1)
root.right = TreeNode(6)
root.right.left = TreeNode(-1)
root.right.right = TreeNode(5)
root.right.right.left = TreeNode(9)
root.right.right.left.left = TreeNode(-2)
root.right.right.right = TreeNode(8)
"""

# this needs more testing
"""
def largestSubBST(root):
    if not root.left and not root.right: return 1,1,root.val,root.val
    left = lMax = right = rMax = 0
    lmn, lmx, rmn, rmx = float('-inf'), root.val-1, root.val+1, float('inf')
    if root.left: lMax,left,lmn,lmx = largestSubBST(root.left)
    if root.right: rMax,right,rmn,rmx = largestSubBST(root.right)
    if left == -1 or right == -1 or not lmx < root.val < rmn: # one or both is none BST
        return max(lMax, rMax), -1, min(root.val,lmn,rmn), max(root.val,lmx,rmx)
    else: # both subtrees are BSTs
        whole = left + right + 1
        return max(whole, lMax, rMax), whole, min(root.val,lmn,rmn), max(root.val,lmx,rmx)
"""
def largestSubBST(root):
    if not root: return 0, 0, float("inf"), -float("inf")
    lMax,left,lmn,lmx = largestSubBST(root.left)
    rMax,right,rmn,rmx = largestSubBST(root.right)
    if left == -1 or right == -1 or not lmx < root.val < rmn: # one/both non-BST or BST broken at node
        return max(lMax, rMax), -1, min(root.val,lmn), max(root.val,rmx)
    whole = left + right + 1
    return max(whole, lMax, rMax), whole, min(root.val,lmn,rmn), max(root.val,lmx,rmx)
"""
      50
   /      \
  30       60
 / \      /  \
5   20   45  70
            /  \
           65  80
"""

root = TreeNode(40)
root.left = TreeNode(30)
root.left.left = TreeNode(5)
root.left.right = TreeNode(35)
root.right = TreeNode(60)
root.right.left = TreeNode(45)
root.right.right = TreeNode(70)
root.right.right.left = TreeNode(65)
root.right.right.right = TreeNode(80)

print(largestSubBST(root)[0])