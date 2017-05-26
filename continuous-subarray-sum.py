# https://leetcode.com/problems/continuous-subarray-sum/#/description
class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        length = len(nums)
        if k == 0:
            for i in range(length):
                if nums[i] == 0 and i+1 < length and nums[i+1] == 0:
                    return True
            return False
        if length < 2:
            return False
        if length == 2:
            if (nums[0]+nums[1]) % k == 0:
                return True
            else:
                return False
            
        k = abs(k)
        s = set()
        running_sum = 0
        for i in range(length):
            running_sum += nums[i]
            remainder = running_sum % k
            if remainder in s:
                return True
            if remainder == 0 and i != 0:
                return True
            s.add(remainder)
        return False