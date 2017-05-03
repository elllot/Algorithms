class TreeNode():
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None

def bottomView(root, nodes, dist):
    if not root: return
    bottomView(root.left, nodes, dist-1)
    bottomView(root.right, nodes, dist+1)
    if dist not in nodes: nodes[dist] = root.val

def topView(root, nodes, dist):
    if not root: return
    topView(root.left, nodes, dist-1)
    topView(root.right, nodes, dist+1)
    nodes[dist] = root.val
    
root = TreeNode(20)
root.left = TreeNode(8)
root.right = TreeNode(22)
root.left.left = TreeNode(5)
root.left.right = TreeNode(3)
root.left.right.left = TreeNode(10)
root.left.right.right = TreeNode(14)
root.right.left = TreeNode(4)
root.right.right = TreeNode(25)

root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)
root2.left.right = TreeNode(4)
root2.left.right.right = TreeNode(5)
root2.left.right.right.right = TreeNode(6)
root2.left.right.right.right.right = TreeNode(7)

view, viewTop = {}, {}
bottomView(root, view, 0)
topView(root2, viewTop, 0)
print([v for k,v in sorted(view.items())])
print([v for k,v in sorted(viewTop.items())])
