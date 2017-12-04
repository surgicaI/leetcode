# https://leetcode.com/problems/implement-strstr/description/
# KMP algorithm
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        kmp = [0]
        i = 1
        j = 0
        while i <len(needle):
            if needle[i] == needle[j]:
                j += 1
                kmp.append(j)
            else:
                while True:
                    j = kmp[j-1]
                    if needle[i] == needle[j]:
                        j += 1
                        kmp.append(j)
                        break
                    if j == 0:
                        kmp.append(j)
                        break
            i += 1
        i = 0

        for index, ch in enumerate(haystack):
            if needle[i] == ch:
                i += 1
            else:
                while True:
                    if i == 0:
                        break
                    i = kmp[i-1]
                    if needle[i] == ch:
                        i += 1
                        break
            if i == len(needle):
                return index - len(needle) + 1
        return -1
