# https://www.interviewbit.com/problems/rotate-matrix/
class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def rotate(self, A):
        n = len(A)
        half1 = n/2
        half2 = n/2 if n%2 == 0 else (n/2 + 1)
        if n > 0:
            for i in range(half1):
                for j in range(half2):
                    temp = A[i][j]
                    A[i][j] = A[n-1-j][i]
                    A[n-1-j][i] = A[n-1-i][n-1-j]
                    A[n-1-i][n-1-j] = A[j][n-1-i]
                    A[j][n-1-i] = temp

        return A