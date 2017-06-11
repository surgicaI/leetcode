# https://leetcode.com/problems/longest-palindromic-subsequence/#/description

class Solution(object):
    def helper(self, i, j):
        if i > j:
            return 0
        if i == j:
            return 0.5
        if self.dict[i][j] != -1:
            return self.dict[i][j]
        if self.s[i] == self.s[j]:
            res = 1 + self.helper(i+1, j-1)
        else:
            res = max(self.helper(i+1, j), self.helper(i, j-1))
        self.dict[i][j] = res
        return res
        
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.dict = [[-1 for _ in s] for __ in s]
        self.s = s
        return int(2 * self.helper(0,len(s)-1))