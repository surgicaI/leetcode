# https://leetcode.com/problems/range-sum-query-2d-immutable/#/description
class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.matrix = matrix
        self.sumMatrix = [[0 for _ in matrix[0]] for __ in matrix]
        for i in range(len(matrix)):
            colsum = 0
            for j in range(len(matrix[0])):
                colsum += matrix[i][j]
                if i != 0:
                    self.sumMatrix[i][j] = colsum + self.sumMatrix[i-1][j]
                else:
                    self.sumMatrix[i][j] = colsum
        print(self.sumMatrix)

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if row1 == row2 and col1 == col2:
            return self.matrix[row1][col1]
        sum = self.sumMatrix[row2][col2]
        if row1-1 >= 0 and col1-1 >= 0:
            sum += self.sumMatrix[row1-1][col1-1]
        if col1-1 >= 0:
            sum -= self.sumMatrix[row2][col1-1]
        if row1-1 >= 0:
            sum-= self.sumMatrix[row1-1][col2]
        return sum


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)