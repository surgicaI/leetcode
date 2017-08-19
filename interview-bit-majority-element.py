# https://www.interviewbit.com/problems/majority-element/

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def majorityElement(self, A):
        my_max = 0
        my_map = {}
        req_freq = len(A) / 2
        for n in A:
            freq = my_map.get(n, 0)
            freq += 1
            my_map[n] = freq
            my_max = max(my_max, freq)
            if my_max > req_freq:
                return n
