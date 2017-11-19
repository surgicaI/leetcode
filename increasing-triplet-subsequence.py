# https://leetcode.com/problems/increasing-triplet-subsequence/description/

class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        current_min = None
        current = None
        supplementry_min = None
        for num in nums:
            if current_min is None:
                current_min = num
            elif current is None and num < current_min:
                current_min = num
            elif current is None and num > current_min:
                current = num
            elif not current is None and num > current:
                return True
            elif not supplementry_min is None and num > supplementry_min:
                current_min = supplementry_min
                current = num
                supplementry_min = None
            elif not current is None and num > current_min and num < current:
                current = num
            elif supplementry_min is None and num < current_min:
                supplementry_min = num
            elif not supplementry_min is None and num < supplementry_min:
                supplementry_min = num
        return False
