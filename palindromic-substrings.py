# https://leetcode.com/problems/palindromic-substrings/description/

class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        cache = collections.Counter()
        for i in range(len(s)):
            cache[s[i]] += 1
            j = 1
            while i-j >= 0 and i+j < len(s) and s[i+j] == s[i-j]:
                j += 1
                cache[s[i-j:i+j+1]] += 1
            j = 0
            while i-j >=0 and i+j+1< len(s) and s[i+j+ 1]== s[i-j]:
                j += 1
                cache[s[i-j:i+j+2]] += 1
        count = 0
        for key, val in cache.items():
            count += val
        return count
