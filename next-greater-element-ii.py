# https://leetcode.com/problems/next-greater-element-ii/#/description

class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        stack = list(reversed(nums))
        res = [-1] * length
        for index in reversed(range(len(nums))):
            while len(stack) > 0 and nums[index] >= stack[-1]:
                stack.pop()
            if len(stack) > 0:
                res[index] = stack[-1]
            stack.append(nums[index])
        return res