# https://leetcode.com/problems/license-key-formatting/#/description

class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        k = K
        res = []
        for c in reversed(S):
            if c != '-':
                if k == 0:
                    k = K
                    res.append('-')
                res.append(c.upper())
                k -= 1

        return ''.join(list(reversed(res)))