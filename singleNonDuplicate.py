# https://leetcode.com/problems/single-element-in-a-sorted-array/#/description
class Solution(object):
    def recursiveSingleNonDuplicate(self,nums):
        if len(nums) == 1 :
            return True,nums[0]
        elif len(nums) == 2 or len(nums)==0:
            return False,0
        n = len(nums)/2
        if nums[n] == nums[n-1]:
            res1,num1 = self.recursiveSingleNonDuplicate(nums[0:n+1])
            res2,num2 = self.recursiveSingleNonDuplicate(nums[n+1:])
            if res1:
                return True, num1
            elif res2:
                return True, num2
            else:
                return False, 0
        elif nums[n] == nums[n+1]:
            res1,num1 = self.recursiveSingleNonDuplicate(nums[0:n])
            res2,num2 = self.recursiveSingleNonDuplicate(nums[n:])
            if res1:
                return True, num1
            elif res2:
                return True, num2
            else:
                return False, 0
        else:
            return True,nums[n]

    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        _,res = self.recursiveSingleNonDuplicate(nums)
        return res
        
