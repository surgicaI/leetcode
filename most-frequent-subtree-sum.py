# https://leetcode.com/problems/most-frequent-subtree-sum/#/description

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.dict = {}
        
    def helper(self, root):
        sum = root.val
        if root.left:
            sum += self.helper(root.left)
        if root.right:
            sum += self.helper(root.right)
        self.dict[sum] = self.dict.get(sum,0) + 1
        return sum
        
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root:
            self.helper(root)
        else:
            return []
        frequent = max(self.dict.values())
        return [i for i,v in self.dict.items() if v==frequent]
            
            