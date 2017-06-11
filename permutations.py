# https://leetcode.com/problems/permutations/#/description

class Solution(object):
    def helper(self, index):
        if index == self.max_index:
            self.res.append(self.nums[:])
        for i in range(index, self.length):
            self.nums[index], self.nums[i] = self.nums[i], self.nums[index]
            self.helper(index+1)
            self.nums[index], self.nums[i] = self.nums[i], self.nums[index]
    
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.max_index = len(nums) - 1
        self.length = len(nums)
        self.nums = nums
        self.res = []
        self.helper(0)
        return self.res