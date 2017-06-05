# https://leetcode.com/problems/integer-break/#/description
# DP Solution

class Solution(object):
    def helper(self,n):
        if n in self.dict:
            return self.dict[n]
        i = 1
        j = n - 1
        res = n
        while j >= i:
            res = max(res,self.helper(i)*self.helper(j))
            i += 1
            j -= 1
        self.dict[n] = res
        return res
        
        
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 3:
            return n-1
        self.dict = {1:1}
        return self.helper(n)
