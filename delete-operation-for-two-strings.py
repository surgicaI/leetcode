# https://leetcode.com/problems/delete-operation-for-two-strings/#/description

class Solution(object):
    def helper(self, word1, word2):
        l1 = len(word1)
        l2 = len(word2)
        if word1 and word2:
            if self.map[l1-1][l2-1]:
                return self.map[l1-1][l2-1]
            if word1[-1] == word2[-1]:
                res = self.helper(word1[:-1],word2[:-1])
            else:
                res = min(self.helper(word1[:-1],word2) + 1, self.helper(word1,word2[:-1]) + 1)
            self.map[l1-1][l2-1] = res
            return res
        else:
            return max(l1,l2)
        
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        self.map = [[0 for _ in word2] for _ in word1]
        return self.helper(list(word1),list(word2))