# https://leetcode.com/problems/add-two-numbers-ii/#/description

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = l1
        l1 = node = None
        while head:
            node = head
            head = head.next
            node.next = l1
            l1 = node
            
        head = l2
        l2 = node = None
        while head:
            node = head
            head = head.next
            node.next = l2
            l2 = node
            
        carry = 0
        ptr1 = l1
        ptr2 = l2
        res = None
        while ptr1 or ptr2 or carry>0:
            sum = carry
            if ptr1:
                sum += ptr1.val
                ptr1 = ptr1.next
            if ptr2:
                sum += ptr2.val
                ptr2 = ptr2.next
            carry = int(sum / 10)
            sum = sum % 10
            node = ListNode(sum)
            node.next = res
            res = node
            
        return res
