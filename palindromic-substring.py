# https://leetcode.com/problems/longest-palindromic-substring/description/
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        best = 0
        res = s[0] if s else ''
        for i in range(len(s)):
            if i-1 >= 0 and i+1 < len(s) and s[i-1]==s[i+1]:
                left = i-1
                right = i+1
                while left-1 >= 0 and right+1 < len(s):
                    if s[left-1] == s[right+1]:
                        left -= 1
                        right += 1
                    else:
                        break
                if right - left + 1 > best:
                    best = right - left + 1
                    res = s[left:right+1]
            if i-1 >= 0 and s[i-1]==s[i]:
                left = i-1
                right = i
                while left-1 >= 0 and right+1 < len(s):
                    if s[left-1] == s[right+1]:
                        left -= 1
                        right += 1
                    else:
                        break
                if right - left + 1 > best:
                    best = right - left + 1
                    res = s[left:right+1]
        return res
