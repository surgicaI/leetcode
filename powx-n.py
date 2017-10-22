# https://leetcode.com/problems/powx-n/description/
class Solution(object):
    def __init__(self):
        self.myMap = {}
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        negetive = False
        if n == 1:
            return x
        if n == 0:
            return 1
        if n in self.myMap:
            return self.myMap[n]
        if n < 0:
            negetive = True
            n = abs(n)
        res = 0
        if n%2 == 0:
            res = self.myPow(x,n/2)*self.myPow(x,n/2)
        else:
            res = self.myPow(x,(n-1)/2)*self.myPow(x,(n-1)/2)*x
        self.myMap[n] = res
        return 1/res if negetive else res
        
