class TreeNode():
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None

def deleteKPath(root, k):
    if not root: return
    deleteK(root, 1, k)

def deleteK(root, depth, k):
    if not root: return -1
    if not root.left and not root.right: return depth
    left, right = deleteK(root.left, depth+1, k), deleteK(root.right, depth+1, k)
    if left < k: root.left = None
    if right < k: root.right = None
    return max(left, right)

def inorder(root, _list):
    if not root: return
    inorder(root.left, _list)
    _list.append(root.val)
    inorder(root.right, _list)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.left.right.left = TreeNode(9)
root.left.left.left = TreeNode(7)
root.right.right = TreeNode(6)
root.right.right.left = TreeNode(8)

l, l2 = [], []
inorder(root, l)
print(l)
deleteKPath(root, 4)
inorder(root, l2)
print(l2)