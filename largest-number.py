# https://leetcode.com/problems/largest-number/#/description
from functools import cmp_to_key

def comp(a,b):
    if a + b > b + a:
        return 1
    elif a + b <= b + a:
        return -1
        
class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        nums = [str(i) for i in nums]
        nums.sort(key=cmp_to_key(comp), reverse = True)
        return ''.join(nums).lstrip('0') or '0'