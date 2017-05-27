# https://leetcode.com/problems/teemo-attacking/#/description
class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        res = 0
        poisonedState = False
        for time in timeSeries:
            if poisonedState:
                if end < time:
                    res += end - start
                    start = time
                    end = time + duration
                else:
                    end = time + duration
            else:
                poisonedState = True
                start = time
                end = time + duration
        if poisonedState:
            res += end - start
            
        return res