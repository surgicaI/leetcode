# https://leetcode.com/problems/add-two-numbers/description/

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
        ptr1 = l1
        ptr2 = l2
        ptr = None
        carry = 0
        while ptr1 or ptr2:
            my_sum = carry
            if ptr1:
                my_sum += ptr1.val
                ptr1 = ptr1.next
            if ptr2:
                my_sum += ptr2.val
                ptr2 = ptr2.next
            carry = my_sum / 10
            temp = ListNode(my_sum % 10)
            if ptr:
                ptr.next = temp
                ptr = temp
            else:
                ptr = temp
                result = ptr
        if carry:
            ptr.next = ListNode(carry)
        return result
