# https://leetcode.com/problems/convert-bst-to-greater-tree/#/description

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self, root, val):
        if not root:
            return 0
        right = self.helper(root.right, val)
        root.val += right + val
        left = self.helper(root.left, root.val)
        return root.val + left - val
        
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.helper(root, 0)
        return root