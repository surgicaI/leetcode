# https://www.interviewbit.com/problems/reverse-link-list-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param m : integer
    # @param n : integer
    # @return the head node in the linked list
    def reverseBetween(self, A, m, n):
        if m == 1:
            previous = None
        else:
            k = 1
            previous = A
            while k < m - 1:
                previous = previous.next
                k += 1
        head = previous.next if not previous is None else A
        ptr1 = head
        ptr2 = head.next
        k = m
        while k < n:
            temp = ptr2.next
            ptr2.next = ptr1
            ptr1 = ptr2
            ptr2 = temp
            k += 1
        if previous is None:
            A = ptr1
        else:
            previous.next = ptr1
        head.next = ptr2
        return A
