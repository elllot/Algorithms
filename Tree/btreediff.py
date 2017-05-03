class TreeNode:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None

def maxDiff(root):
    if not root: return -float("inf"), float("inf")
    diffLeft, lMin = maxDiff(root.left)
    diffRight, rMin = maxDiff(root.right)
    localMaxLeft = max(root.val - lMin, diffLeft)
    localMaxRight = max(root.val - rMin, diffRight)
    return max(localMaxLeft, localMaxRight), min(root.val, lMin, rMin)

def minDiff(root):
    if not root: return float("inf"), -float("inf")
    diffLeft, lMax = minDiff(root.left)
    diffRight, rMax = minDiff(root.right)
    localMinLeft = min(root.val - lMax, diffLeft)
    localMinRight = min(root.val - rMax, diffRight)
    return min(localMinLeft, localMinRight), max(root.val, lMax, rMax) 

#def maxDiffAny():

root = TreeNode(8)
root.left = TreeNode(3)
root.right = TreeNode(10)
root.left.left = TreeNode(1)
root.left.right = TreeNode(6)
root.left.right.left = TreeNode(4)
root.left.right.right = TreeNode(7)
root.right = TreeNode(10)
root.right.right = TreeNode(14)
root.right.right.left = TreeNode (13)

print(maxDiff(root)[0])
print(minDiff(root)[0])