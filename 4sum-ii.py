# https://leetcode.com/problems/4sum-ii/#/description

class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        dict = {}
        for a in A:
            for b in B:
                dict[a+b] = dict.get(a+b,0) + 1
        res = 0
        for c in C:
            for d in D:
                res += dict.get(-1*(c+d),0)
        return res