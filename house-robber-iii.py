# https://leetcode.com/problems/house-robber-iii/#/description

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def helper(self, root):
        if root in self.dict:
            return self.dict[root]
        res = root.val 
        if root.left:
            res += self.helper(root.left.left) + self.helper(root.left.right)
        if root.right:
            res += self.helper(root.right.left) + self.helper(root.right.right)
        self.dict[root] = max(res, self.helper(root.left) + self.helper(root.right))
        return self.dict[root]

    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.dict = {None : 0}
        return self.helper(root)