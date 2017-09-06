# https://www.interviewbit.com/problems/max-non-negative-subarray/

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        my_sum = None
        start = None
        length = None
        current_start = None
        current_sum = None
        for index, n in enumerate(A):
            if current_start is None and n >= 0:
                current_start = index
                current_sum = n
            elif n >= 0:
                current_sum += n
            elif n < 0:
                if not current_start is None:
                    if my_sum is None or current_sum > my_sum or (current_sum == my_sum and length < index-current_start):
                        my_sum = current_sum
                        start = current_start
                        length = index - current_start
                    current_start = None
                    current_sum = None

        if not current_start is None:
            if my_sum is None or current_sum > my_sum or (current_sum == my_sum and length < len(A)-current_start):
                my_sum = current_sum
                start = current_start
                length = len(A) - current_start
            current_start = None
            current_sum = None

        return A[start:start+length] if not start is None else []
