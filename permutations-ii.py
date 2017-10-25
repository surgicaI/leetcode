# https://leetcode.com/problems/permutations-ii/description/

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.counter = {}
        self.results = []
        self.length = len(nums)
        for num in nums:
            self.counter[num] = self.counter.get(num, 0) + 1
        self.helper([])
        return self.results

    def helper(self, result):
        if len(result) == self.length:
            self.results.append(copy.copy(result))
            return
        for num, count in self.counter.items():
            count -= 1
            if count == 0:
                self.counter.pop(num)
            else:
                self.counter[num] = count
            result.append(num)
            self.helper(result)
            num = result.pop()
            self.counter[num] = self.counter.get(num, 0) + 1
