https://www.interviewbit.com/problems/sort-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def sortList(self, A):
        ptr = A
        n = 0
        while not ptr is None:
            ptr = ptr.next
            n += 1
        return self.mySort(A, n)

    def mySort(self, A, n):
        if n == 1:
            return A
        i = 1
        ptr = A
        while i < n / 2:
            ptr = ptr.next
            i += 1
        B = ptr.next
        ptr.next = None
        return self.merge(self.mySort(A, i), self.mySort(B, n-i))

    def merge(self, A, B):
        a = A
        b = B
        head = None
        while not a is None and not b is None:
            if a.val < b.val:
                if head is None:
                    head = a
                    ptr = head
                else:
                    ptr.next = a
                    ptr = ptr.next
                a = a.next
            else:
                if head is None:
                    head = b
                    ptr = head
                else:
                    ptr.next = b
                    ptr = ptr.next
                b = b.next
        if not a is None or not b is None:
            ptr.next = a if not a is None else b
        return head
