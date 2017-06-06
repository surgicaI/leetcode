# https://leetcode.com/problems/is-subsequence/#/description

#follow up with Binary Search

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not s:
            return True
        index = 0
        length = len(s)
        for ch in t:
            if ch == s[index]:
                index += 1
            if index == length:
                return True
        return False