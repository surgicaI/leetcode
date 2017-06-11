# https://leetcode.com/problems/odd-even-linked-list/#/description

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        odd = head
        even = even_head = head.next
        odd_ptr = even.next if even else None
        even_ptr = odd_ptr.next if odd_ptr else None
        while odd_ptr or even_ptr:
            odd.next = odd_ptr
            even.next = even_ptr
            odd_ptr = even_ptr.next if even_ptr else None
            even_ptr = odd_ptr.next if odd_ptr else None
            odd = odd.next
            even = even.next
        odd.next = even_head
        return head
        