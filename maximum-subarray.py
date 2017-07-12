# https://leetcode.com/problems/maximum-subarray/#/description

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maximum = -(2**63)
        Sum = 0
        for num in nums:
            Sum += num
            maximum = max(maximum, Sum)
            if Sum < 0:
                Sum = 0
        return maximum
