# https://leetcode.com/problems/find-bottom-left-tree-value/#/description

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self, node, level):
        if (not node.left) and (not node.right):
            return node.val, level
        if node.left:
            val_left, level_left = self.helper(node.left, level + 1)
        if node.right:
            val_right, level_right = self.helper(node.right, level + 1)
        if not node.left:
            return val_right, level_right
        elif not node.right:
            return val_left, level_left
        else:
            return (val_left, level_left) if level_left >= level_right else (val_right, level_right)
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        val, lvl = self.helper(root, 0)
        return val