# https://leetcode.com/problems/top-k-frequent-elements/#/description

import collections
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        my_counter = collections.Counter()
        for num in nums:
            my_counter[num] += 1
        my_list = my_counter.items()
        my_list.sort(reverse=True, key = lambda x: x[1])
        res = []
        for i in range(k):
            res.append(my_list[i][0])
        return res


# solution 2
import collections
class Solution(object):
    def topKFrequent(self, nums, k):
        bucket = [[] for _ in nums]
        for num, freq in collections.Counter(nums).items():
            bucket[-freq].append(num)
        return list(itertools.chain.from_iterable(bucket))[:k]