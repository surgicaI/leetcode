# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        ptr = head
        remove = False

        while ptr and ptr.next:
            if ptr.val == ptr.next.val:
                remove = True
                ptr = ptr.next
            else:
                temp = ptr
                ptr = ptr.next
                if remove:
                    if prev:
                        prev.next = ptr
                    else:
                        head = ptr
                    remove = False
                else:
                    prev = temp
        if remove:
            if prev:
                prev.next = None
            else:
                head = None
        return head
