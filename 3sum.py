# https://leetcode.com/problems/3sum/#/description
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()
        length = len(nums)
        for i in range(length):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            if nums[i] > 0:
                break
            j = i+1
            k = length-1
            while j < k :
                sum = nums[i] + nums[j] + nums[k]
                if sum > 0:
                    while True:
                        k -= 1
                        if k == 0 or nums[k] != nums[k+1]:
                            break
                elif sum < 0:
                    while True:
                        j += 1
                        if j == length-1 or nums[j] != nums[j-1]:
                            break
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    while True:
                        k -= 1
                        if k == 0 or nums[k] != nums[k+1]:
                            break
                    while True:
                        j += 1
                        if j == length-1 or nums[j] != nums[j-1]:
                            break
        
        return result