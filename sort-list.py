# https://leetcode.com/problems/sort-list/description/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        length = 0
        ptr = head
        while ptr:
            length += 1
            ptr = ptr.next
        return self.sort(head, length)

    def sort(self, node, length):
        if length <= 1:
            return node
        left = int(length / 2)
        right = length - left
        nodeRight = node
        for i in range(left):
            if i == left - 1:
                temp = nodeRight.next
                nodeRight.next = None
                nodeRight = temp
            else:
                nodeRight = nodeRight.next
        return self.merge(self.sort(node, left), self.sort(nodeRight, right))

    def merge(self, node1, node2):
        head = None
        while node1 and node2:
            if node1.val < node2.val:
                if head is None:
                    head = node1
                    ptr = head
                else:
                    ptr.next = node1
                    ptr = ptr.next
                node1 = node1.next
            else:
                if head is None:
                    head = node2
                    ptr = node2
                else:
                    ptr.next = node2
                    ptr = ptr.next
                node2 = node2.next
        ptr.next = node1 if node1 else node2
        return head
