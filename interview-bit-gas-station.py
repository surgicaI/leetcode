# https://www.interviewbit.com/problems/gas-station/

class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return an integer
    def canCompleteCircuit(self, A, B):
        result = index = 0
        gas = 0
        while True:
            gas = gas + A[index] - B[index]
            index = (index + 1) % len(A)
            if gas < 0:
                if result < index:
                    result = index
                    gas = 0
                else:
                    return -1
            elif result == index:
                return result
