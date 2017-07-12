# https://leetcode.com/problems/rotate-function/#/description

class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        length = len(A)
        SUM = sum(A)
        result = value = sum([n*A[n] for n in range(length)])
        for i in reversed(range(length)):
            value = value + SUM - (A[i]*length)
            result = max(result, value)
        return result
