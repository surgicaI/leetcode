# https://leetcode.com/problems/array-nesting/#/description

class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        length = len(nums)
        index = 0
        chain = 1
        while index < length:
            if index == nums[index]:
                index += 1
                res = max(res,chain)
                chain = 1
            else:
                val = nums[index]
                nums[index], nums[val] = nums[val], nums[index]
                chain += 1
        return res