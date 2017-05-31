# https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/#/description

class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        nums.sort()
        j = len(nums) - 1
        i = 0
        while j > i:
            res += nums[j] - nums[i]
            i += 1
            j -= 1
        return res