# https://leetcode.com/problems/product-of-array-except-self/#/description

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        res = [1]*length
        left = 1
        right = 1
        indices = range(length)
        for i,j in zip(indices, reversed(indices)):
            res[i] *= left
            res[j] *= right
            left *= nums[i]
            right *= nums[j]
        return res
            