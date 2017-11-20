# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/description/

# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root is None:
            return
        self.leftNodes = []
        self.helper(root, 0)

    def helper(self, node, level):
        if not node or (not node.left and not node.right):
            return
        if len(self.leftNodes) >= level + 1:
            self.leftNodes[level].next = node.left or node.right
            self.leftNodes[level] = node.right or node.left
        else:
            self.leftNodes.append(node.right or node.left)
        if node.left:
            node.left.next = node.right
        self.helper(node.left, level+1)
        self.helper(node.right, level+1)
