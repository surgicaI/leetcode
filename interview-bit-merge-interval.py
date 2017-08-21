# https://www.interviewbit.com/problems/merge-intervals/

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param new_interval, a Interval
    # @return a list of Interval
    def insert(self, intervals, new_interval):
        start = None
        end = None
        if new_interval.start > new_interval.end:
            new_interval.start, nre_interval.end = new_interval.end, new_interval.start
        for interval in intervals:
            if self.isOverlap(interval, new_interval):
                if start is None:
                    start = min(interval.start, new_interval.start)
                end = max(interval.end, new_interval.end)
        result = []
        if not start is None:
            result_interval = Interval(start, end)
        else:
            if not intervals or intervals[0].start > new_interval.end:
                result.append(new_interval)
            for index, interval in enumerate(intervals):
                result.append(interval)
                if new_interval.start > interval.end and (index == len(intervals) - 1 or new_interval.end < intervals[index+1].start):
                    result.append(new_interval)
            return result
        added = False
        for interval in intervals:
            if self.isOverlap(interval, result_interval):
                if not added:
                    result.append(result_interval)
                    added = True
                else:
                    continue
            else:
                result.append(interval)
        return result

    def isOverlap(self, i1, i2):
        if i1.start <= i2.end and i1.start >= i2.start:
            return True
        if i2.start >= i1.start and i2.start <= i1.end:
            return True
        return False
