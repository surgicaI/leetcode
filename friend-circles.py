# https://leetcode.com/problems/friend-circles/#/description

class Solution(object):
    def add(self, M, index):
        self.not_added[index] = 0
        for i in range(self.length):
            if M[index][i] == 1 and self.not_added[i]:
                self.add(M, i)
                
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        self.length = len(M)
        self.not_added = [1]*self.length
        circles = 0
        for i in range(self.length):
            if self.not_added[i]:
                circles += 1
                self.add(M,i)
        return circles