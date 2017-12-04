# https://leetcode.com/problems/largest-rectangle-in-histogram/description/

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = []
        res = 0
        numHeights = len(heights)
        for index, height in enumerate(heights):
            while stack and stack[-1][1] > height:
                i, h = stack.pop()
                startIndex = stack[-1][0] + 1 if stack else 0
                area = h*(index - startIndex)
                res = max(res, area)
            stack.append((index, height))
        while stack:
            index, height = stack.pop()
            startIndex = stack[-1][0] + 1 if stack else 0
            area = height * (numHeights - startIndex)
            res = max(res, area)
        return res
        
