class Node:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None
        self.next = None
        self.prev = None

def convert(root):
    if not root: return
    if root.left:
        p = root.left
        while p.right:
            p = p.right
        temp, root.left, p.right = root.left, None, root
        return convert(temp)
    # Assigning pointers
    root.next = convert(root.right)
    if root.next: root.next.prev = root
    return root

root = Node(4)
root.left = Node(2)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(5)
root.right.right = Node(7)
head = convert(root)
while head:
    print(head.val)
    head = head.next
