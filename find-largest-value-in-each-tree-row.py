# https://leetcode.com/problems/find-largest-value-in-each-tree-row/#/description

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.res = []
    def largestValues(self, root, level=0):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        if len(self.res) == level:
            self.res.append(root.val)
        else:
            if self.res[level] < root.val:
                self.res[level] = root.val
        self.largestValues(root.left, level + 1)
        self.largestValues(root.right, level + 1)
        return self.res
        