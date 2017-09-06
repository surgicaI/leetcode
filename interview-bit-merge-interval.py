# https://www.interviewbit.com/problems/merge-intervals/

# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param new_interval, a Interval
    # @return a list of Interval
    def insert(self, intervals, new_interval):
        result = []
        if new_interval.end < new_interval.start:
            new_interval.start, new_interval.end = new_interval.end, new_interval.start
        if not intervals or intervals[0].start > new_interval.end:
            result.append(new_interval)
            result.extend(intervals)
            return result
        if new_interval.start > intervals[-1].end:
            result.extend(intervals)
            result.append(new_interval)
            return result
        start = None
        end = None
        added = False
        for index,interval in enumerate(intervals):
            if self.isOverlap(interval, new_interval):
                if start is None:
                    start = min(interval.start, new_interval.start)
                end = max(interval.end, new_interval.end)
            else:
                if not start is None and not added:
                    result.append(Interval(start, end))
                    added = True
                result.append(interval)
                if new_interval.start > interval.end and new_interval.end < intervals[index+1].start:
                    result.append(new_interval)
        if not start is None and not added:
            result.append(Interval(start, end))
        return result

    def isOverlap(self, i1, i2):
        if i1.start >= i2.start and i1.start <= i2.end:
            return True
        if i2.start >= i1.start and i2.start <= i1.end:
            return True
        return False
