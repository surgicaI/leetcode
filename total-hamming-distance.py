# https://leetcode.com/problems/total-hamming-distance/#/description

class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        length = len(nums)
        for i in range(32):
            count = 0
            for num in nums:
                count += (num >> i) & 1 
            res += count * (length - count)
        return res