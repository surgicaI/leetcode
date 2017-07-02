# https://leetcode.com/problems/kth-smallest-element-in-a-bst/#/description

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def helper(self, node):
        if node.left:
            self.helper(node.left)
        if self.k == 0:
            return
        self.k -= 1
        if self.k == 0:
            self.result = node.val
            return
        if node.right:
            self.helper(node.right)

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.k = k
        self.helper(root)
        return self.result
