# https://leetcode.com/problems/combination-sum-iv/#/description

class Solution(object):
    def __init__(self):
        self.dict = {}
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in self.dict:
            return self.dict[target]
        res = 0
        for num in nums:
            val = target - num
            if val == 0:
                res += 1
            if val > 0:
                res += self.combinationSum4(nums, val)
        self.dict[target] = res
        return res