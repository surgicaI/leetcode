# https://leetcode.com/problems/word-search-ii/description/
class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        trie = {}
        self.result = set()
        self.numRows = len(board)
        self.numCols = len(board[0]) if self.numRows else 0
        self.visited  = [[False]*self.numCols for _ in range(self.numRows)]
        self.board = board
        for word in words:
            myNode = trie
            for index, ch in enumerate(word):
                if ch in myNode:
                    myNode = myNode[ch]
                else:
                    myNode[ch] = {}
                    myNode = myNode[ch]
                if index == len(word)-1:
                    myNode['END'] = None
        for i, row in enumerate(board):
            for j, ch in enumerate(row):
                if ch in trie:
                    self.verify(i,j, trie[ch], [ch])
        return list(self.result)

    def verify(self, i, j, node, word):
        self.visited[i][j] = True
        points = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
        if 'END' in node:
            self.result.add(''.join(word))
        for x, y in points:
            if x < 0 or x >= self.numRows or y < 0 or y >= self.numCols or self.visited[x][y]:
                continue
            ch = self.board[x][y]
            if ch in node:
                self.verify(x, y, node[ch], word + [ch])
        self.visited[i][j] = False
