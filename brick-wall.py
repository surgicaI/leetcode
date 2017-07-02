# https://leetcode.com/problems/brick-wall/#/description
import collections


class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        result = collections.Counter()
        for layer in wall:
            position = 0
            for brick in layer[:-1]:
                position += brick
                result[position] += 1
        return len(wall) - (max(result.values()) if result.values() else 0)
