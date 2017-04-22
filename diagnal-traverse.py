#https://leetcode.com/problems/diagonal-traverse/#/description
class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        rows = len(matrix)
        if rows == 0:
            return res
        cols = len(matrix[0])
        pos = False
        for i in range(rows+cols-1):
            if pos:
                if i >= cols:
                    c = cols-1
                    r = i-c
                else:
                    c = i
                    r = 0
            else:
                if i >= rows:
                    r = rows - 1
                    c = i - r
                else:
                    r = i
                    c = 0
            while True:
                res.append(matrix[r][c])
                if pos:
                    c -= 1
                    r += 1
                else :
                    c += 1
                    r -= 1
                if r < 0 or c < 0 or r >= rows or c >= cols:
                    break;
            pos = not pos
        return res
            
            