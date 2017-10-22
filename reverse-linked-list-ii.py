# https://leetcode.com/problems/reverse-linked-list-ii/description/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        ptr = head
        numNode = 1
        prev = None
        headConnect = None
        tailConnect = None
        end = None
        begin = None
        while ptr:
            if numNode == m:
                headConnect = prev
                end = ptr
            if numNode == n:
                tailConnect = ptr.next
                begin = ptr
            if numNode >=m and numNode<=n:
                temp = ptr.next
                ptr.next = prev
                prev = ptr
                ptr = temp
            else:
                prev = ptr
                ptr = ptr.next
            numNode += 1
        if headConnect:
            headConnect.next = begin
        else:
            head = begin
        end.next = tailConnect
        return head
