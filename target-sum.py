# https://leetcode.com/problems/target-sum/#/description

class Solution(object):
    def helper(self, index, Sum):
        key = (index,Sum)
        if index == self.length:
            if not Sum:
                return 1
            else:
                return 0
        else:
            if key in self.dict:
                return self.dict[key]
            res = self.helper(index+1, Sum + self.nums[index]) + self.helper(index+1, Sum - self.nums[index])
            self.dict[key] = res
            return res
            

    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        self.dict = {}
        self.nums = nums
        self.length = len(nums)
        return self.helper(0,S)
