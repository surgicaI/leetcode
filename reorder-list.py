# https://leetcode.com/problems/reorder-list/description/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import math
class Solution(object):
    def reverse(self, head):
        ptr = head
        prev = None
        while ptr:
            temp = ptr.next
            ptr.next = prev
            prev = ptr
            ptr = temp
        return prev
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        length = 0
        ptr = head
        while ptr:
            ptr = ptr.next
            length += 1
        if length > 2:
            m = 1
            ptr = head
            length = int(math.ceil(float(length) / 2))
            while m < length:
                ptr = ptr.next
                m += 1
            head2 = self.reverse(ptr.next)
            ptr.next = None
            ptr1 = head
            ptr2 = head2
            while ptr1 and ptr2:
                temp1 = ptr1.next
                temp2 = ptr2.next
                ptr1.next = ptr2
                ptr2.next = temp1
                ptr1 = temp1
                ptr2 = temp2

        
