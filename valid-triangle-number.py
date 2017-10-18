# https://leetcode.com/problems/valid-triangle-number/description/

class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        count = 0
        for i in range(len(nums)-2):
            j = i+1
            k = j+1
            while j<k and k<len(nums):
                if nums[i] + nums[j] > nums[k]:
                    count += (k-j)
                    k += 1
                else:
                    j += 1
                    if j == k:
                        k += 1
        return count
