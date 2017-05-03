class TreeNode():
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None

def fullBTree(root):
    if not root: return True
    if not root.left and not root.right: return True
    if not root.left or not root.right: return False
    return fullBTree(root.left) and fullBTree(root.right)

root = TreeNode(1)
root.left = TreeNode()
root.right = TreeNode()
root.left.left = TreeNode()
root.left.right = TreeNode()
root.right.left = TreeNode()
root.right.right = TreeNode()

print(fullBTree(root))