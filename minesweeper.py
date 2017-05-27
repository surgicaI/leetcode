# https://leetcode.com/problems/minesweeper/#/description

class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        rows = len(board)
        if rows == 0:
            return board
        cols = len(board[0])
        x,y = click
        if board[x][y] == 'M':
            board[x][y] = 'X'
            return board
        elif board[x][y] != 'E':
            return board
        mines = 0
        for i in [x-1,x,x+1]:
            if i < 0 or i >= rows:
                continue
            for j in [y-1,y,y+1]:
                if j < 0 or j >= cols:
                    continue
                if board[i][j] == 'M':
                    mines += 1
        if mines == 0:
            board[x][y] = 'B'
            for i in [x-1,x,x+1]:
                if i < 0 or i >= rows:
                    continue
                for j in [y-1,y,y+1]:
                    if j < 0 or j >= cols:
                        continue
                    self.updateBoard(board,[i,j])
        else:
            board[x][y] = str(mines)
        return board
                