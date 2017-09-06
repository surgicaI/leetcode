# https://www.interviewbit.com/problems/grid-unique-paths/

class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def uniquePaths(self, A, B):
        matrix = []
        for i in range(B):
            matrix.append([0 for _ in range(A)])
        matrix[B-1][A-1] = 1
        for i in range(B-1, -1, -1):
            for j in range(A-1, -1, -1):
                if matrix[i][j] == 0:
                    if i+1 < B:
                        matrix[i][j] += matrix[i+1][j]
                    if j+1 < A:
                        matrix[i][j] += matrix[i][j+1]
        return matrix[0][0]
