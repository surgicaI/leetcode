# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/#/description

from heapq import heappush, heappop
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        length = len(matrix)
        heap = [(matrix[0][0], 0, 0)]
        marker = matrix[0][0] - 1
        k -= 1
        while k:
            _, i, j = heappop(heap)
            if i+1 < length and matrix[i+1][j] != marker:
                heappush(heap,(matrix[i+1][j], i+1 , j))
                matrix[i+1][j] = marker
            if j+1 < length and matrix[i][j+1] != marker:
                heappush(heap, (matrix[i][j+1], i, j+1))
                matrix[i][j+1] = marker
            k -= 1
        val, _, __ = heappop(heap)
        return val