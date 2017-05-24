# https://leetcode.com/problems/contains-duplicate-iii/#/description
class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if t < 0 or k < 0:
            return False
        n = len(nums)
        div = t+1
        dict = {}
        for i in xrange(n):
            temp = nums[i] / div
            if temp in dict:
                return True
            if (temp - 1 in dict) and abs(dict[temp-1]-nums[i]) <= t:
                return True
            if (temp + 1 in dict) and abs(dict[temp+1]-nums[i]) <= t:
                return True
            dict[temp] = nums[i]
            if i >= k:
                dict.pop(nums[i-k]/div)
        return False
                