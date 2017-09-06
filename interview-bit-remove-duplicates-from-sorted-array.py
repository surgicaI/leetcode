# https://www.interviewbit.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        i = 0
        for j,n in enumerate(A):
            if A[i] != A[j]:
                i += 1
                A[i] = A[j]
        A = A[:i+1]
        return i+1
