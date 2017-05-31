# https://leetcode.com/problems/arithmetic-slices/#/description

class Solution(object):
    def __init__(self):
        self.dict = {}
        
    def helper(self, n):
        if n in self.dict:
            return self.dict[n]
        res = 0
        for i in xrange(3,n+1):
            res += n-i+1
        self.dict[n] = res
        return res
        
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        slice = 2
        res = 0
        d = None
        for i in range(1, len(A)):
            if d == A[i] - A[i-1]:
                slice += 1
            else:
                d = A[i] - A[i-1]
                if slice > 2:
                    res += self.helper(slice)
                    slice = 2

        res += self.helper(slice)

        return res
        