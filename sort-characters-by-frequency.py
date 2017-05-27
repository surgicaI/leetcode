# https://leetcode.com/problems/sort-characters-by-frequency/#/description

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        dict = {}
        for char in s:
            dict[char] = dict.get(char,0) + 1
        new_s = list(dict.items())
        new_s.sort(reverse=True, key=lambda x: x[1])
        res = [''.join([i]*j) for i,j in new_s]
        return ''.join(res)
        