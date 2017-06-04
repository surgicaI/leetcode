# https://leetcode.com/problems/minimum-time-difference/#/description

class Solution(object):
    def diff(self, time1, time2):
        hrs1,mins1 = time1.split(':')
        hrs2,mins2 = time2.split(':')
        t1 = int(hrs1)*60 + int(mins1)
        t2 = int(hrs2)*60 + int(mins2)
        res = abs(t1 - t2)
        return min(res, self.max_mins - res)
        
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        res = self.max_mins = 24 * 60
        timePoints.sort()
        for i in range(len(timePoints)):
            res = min(self.diff(timePoints[i],timePoints[i-1]), res)
        return res