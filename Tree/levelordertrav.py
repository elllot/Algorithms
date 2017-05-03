class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BTree:
    def __init__(self):
        self.root = None

    def buildTree(self, arr):
        self.root = None

def levelorderTrav(root):
    if not root: return []
    stack, rList = [], []
    stack.append(root)
    while stack:
        temp = []
        for i in range(len(stack)):
            node = stack.pop()
            temp.append(node.val)
            if node.right: stack.append(node.right)
            if node.left: stack.append(node.left)
        rList.append(temp)
    return rList

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print(levelorderTrav(root))