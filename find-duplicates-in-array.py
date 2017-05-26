# https://leetcode.com/problems/find-all-duplicates-in-an-array/#/description
class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        index = 0
        while index < len(nums):
            a = nums[index]
            if a == index+1:
                index += 1
            else:
                if a == nums[a-1]:
                    index +=1
                    continue
                nums[index],nums[a-1] = nums[a-1],nums[index]
        res = []
        for i in range(len(nums)):
            a = nums[i]
            if a != (i+1):
                res.append(a)
                
        return res