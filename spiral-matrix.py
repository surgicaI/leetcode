# https://leetcode.com/problems/spiral-matrix/#/description
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        rows = len(matrix)
        if rows == 1:
            return matrix[0]
        if rows == 0:
            return []
        cols = len(matrix[0])
        if cols == 0:
            return []
        elements = rows * cols
        result = []
        min_r = 0
        min_c = 0
        max_r = rows-1
        max_c = cols-1
        r = min_r
        c = min_c
        direction = 'right'
        for i in range(elements):
            result.append(matrix[r][c])
            if direction == 'right':
                if c == max_c:
                    direction = 'down'
                    min_r += 1
                    r += 1
                else:
                    c += 1
            elif direction == 'down':
                if r == max_r:
                    direction = 'left'
                    max_c -= 1
                    c -= 1
                else:   
                    r += 1
            elif direction == 'left':
                if c == min_c:
                    direction = 'up'
                    max_r -= 1
                    r -= 1
                else:
                    c -= 1
            elif direction == 'up':
                if r == min_r:
                    direction = 'right'
                    min_c += 1
                    c += 1
                else:
                    r -= 1
            
        return result