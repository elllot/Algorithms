# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution(object):
    def findBottomLeftValue(self, root):
        """
        : Return the leftmost leaf given a binary tree (not necessarily a BST)
        :type root: TreeNode
        :rtype: int
        """
        pQue = deque()
        pQue.append(root)
        rVal = 0
        while pQue:
            node = pQue.popleft()
            if not node: continue
            rVal = node.val
            pQue.append(node.right)
            pQue.append(node.left)
        return rVal