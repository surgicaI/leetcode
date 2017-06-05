# https://leetcode.com/problems/binary-tree-inorder-traversal/#/description

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        visited = set()
        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            if node in visited:
                res.append(node.val)
            elif node:
                visited.add(node)
                stack.extend([node.right, node, node.left])
        return res
                