# https://leetcode.com/problems/subarray-sum-equals-k/#/description

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sums = {}
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            l = sums.get(sum,[])
            l.append(i)
            sums[sum] = l
        res = 0
        sum = 0
        for i in range(len(nums)):
            indices = sums.get(sum+k, [])
            for x in indices:
                res += 1 if x >= i else 0
            sum += nums[i]
        return res