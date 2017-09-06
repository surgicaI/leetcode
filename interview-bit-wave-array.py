# https://www.interviewbit.com/problems/wave-array/

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def wave(self, A):
        A.sort()
        result = []
        index = 1
        while index < len(A):
            result.append(A[index])
            result.append(A[index-1])
            index += 2
        if len(result) < len(A):
            result.append(A[-1])
        return result
