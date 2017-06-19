# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def helper(self, node, v, d):
        if not node:
            return
        if d == 2:
            left = TreeNode(v)
            right = TreeNode(v)
            left.left = node.left
            right.right = node.right
            node.left = left
            node.right = right
            return
        self.helper(node.left, v, d-1)
        self.helper(node.right, v, d-1)

    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if d == 1:
            head = TreeNode(v)
            head.left = root
            return head
        self.helper(root, v, d)
        return root
