# https://leetcode.com/problems/predict-the-winner/#/description

class Solution(object):
    def helper(self, i, j):
        key = str(i)+str(j)
        if key in self.dict:
            return self.dict[key]
        if i == j:
            return [self.nums[i], 0]
        [res1_1, res1_2] = self.helper(i+1, j)
        [res2_1, res2_2] = self.helper(i, j-1)
        res1_2 += self.nums[i]
        res2_2 += self.nums[j]
        self.dict[key] = [res1_2, res1_1] if res1_2  > res2_2 else [res2_2, res2_1]
        return self.dict[key]
        
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        self.nums = nums
        self.dict = {}
        score1, score2  = self.helper(0,len(nums)-1)
        return score1>=score2