# https://leetcode.com/problems/surrounded-regions/#/description
class Solution(object):
    def add(self, i, j):
        newpoints = [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]
        for x,y in newpoints:
            if x < 0 or x >= self.rows or y < 0 or y>=self.cols:
                continue
            self.points.append((x,y))
            
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.rows = len(board)
        if self.rows != 0 :
            self.cols = len(board[0])
        else:
            return
        marked = [[False for _ in range(self.cols)] for __ in range(self.rows)]
        
        self.points = [(0,j) for j in range(self.cols)] + [(self.rows-1,j) for j in range(self.cols)] + [(i,0) for i in range(self.rows)] + [(i,self.cols-1) for i in range(self.rows)]
        while len(self.points) > 0:
            i,j = self.points.pop()
            if board[i][j] == 'O' and not marked[i][j]:
                marked[i][j] = True
                self.add(i, j)
        
        for i in range(self.rows):
            for j in range(self.cols):
                if not marked[i][j]:
                    board[i][j] = 'X'
                