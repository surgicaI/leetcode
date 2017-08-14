# https://leetcode.com/problems/longest-consecutive-sequence/description/
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        my_map = {}
        my_set = set()
        result = 0
        for n in nums:
            if n in my_set:
                continue
            my_set.add(n)
            if n-1 in my_map and n+1 in my_map:
                num = my_map[n-1]
                if num is None:
                    lis1 = [n-1, n]
                    num = n-1
                else:
                    lis1 = my_map[num] + [n]
                lis2 = my_map[n+1]
                if lis2 is None:
                    lis2 = [n+1]
                lis = lis1 + lis2
                result = max(result, len(lis))
                my_map.pop(n-1)
                my_map.pop(n+1)
                my_map[lis[-1]] = num
                my_map[num] = lis
            elif n-1 in my_map:
                num = my_map[n-1]
                if not num is None:
                    lis = my_map[num]
                    lis.append(n)
                    result = max(result, len(lis))
                    my_map[n] = num
                    my_map.pop(n-1)
                    my_map[num] = lis
                else:
                    lis = [n-1, n]
                    my_map[n-1] = lis
                    result = max(result, len(lis))
                    my_map[n] = n-1
            elif n+1 in my_map:
                lis = my_map[n+1]
                if lis is None:
                    my_map[n+1] = n
                    lis = [n+1]
                else:
                    my_map.pop(n+1)
                lis = [n] + lis
                my_map[n] = lis
                my_map[lis[-1]] = n
                result = max(result, len(lis))
            else:
                my_map[n] = None
                result = max(result, 1)
        return result
