# https://leetcode.com/problems/zigzag-conversion/#/solutions
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        result = [[] for _ in range(numRows)]
        down = True
        index = 0
        for char in s:
            result[index].append(char)
            if down:
                index += 1
                if index == numRows - 1:
                    down = False
            else:
                index -= 1
                if index == 0:
                    down = True
        return ''.join([''.join(x) for x in result])