# https://leetcode.com/problems/remove-k-digits/description/

# using statck
class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        result = []
        for n in num:
            while k and result and result[-1] > n:
                result.pop()
                k -= 1
            result.append(n)
        result = ''.join(result[:-k]) if k else ''.join(result)
        return str(int(result)) if result else '0'

## SOLUTION-2 ##
# using doubly linked list
from collections import deque
class Node:
    def __init__(self, n):
        self.val = n
        self.prev = None
        self.next = None
class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        if not num:
            return num
        head = None
        ptr = None
        for n in num:
            node = Node(n)
            if not head:
                head = node
                ptr = node
            else:
                ptr.next = node
                node.prev = ptr
                ptr = node
        ptr = head
        while ptr:
            temp = ptr.prev
            if temp and temp.val > ptr.val:
                ptr.prev = temp.prev
                if ptr.prev == None:
                    head = ptr
                else:
                    ptr.prev.next = ptr
                k -= 1
            else:
                ptr = ptr.next
            if k == 0:
                break
        ptr = head
        result = []
        while ptr:
            result.append(ptr.val)
            ptr = ptr.next
        result = ''.join(result[:-k]) if k else ''.join(result)
        return str(int(result)) if result else '0'
