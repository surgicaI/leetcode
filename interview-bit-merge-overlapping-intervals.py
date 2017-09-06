# https://www.interviewbit.com/problems/merge-overlapping-intervals/

# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @return a list of Interval
    def merge(self, intervals):
        intervals.sort(key=lambda x:(x.start, x.end))
        new_interval = None
        result = []
        for index, interval in enumerate(intervals):
            if new_interval is None:
                new_interval = interval
            elif self.isOverlap(new_interval, interval):
                new_interval.end = max(interval.end, new_interval.end)
            else:
                result.append(new_interval)
                new_interval = interval
        if not new_interval is None:
            result.append(new_interval)
        return result

    def isOverlap(self, i1, i2):
        if i1.start >= i2.start and i1.start <= i2.end:
            return True
        if i2.start >= i1.start and i2.start <= i1.end:
            return True
        return False
