# https://www.interviewbit.com/problems/regular-expression-ii/

class Solution:
    def isMatch(self, A, B, index_s=0, index_r=0):
        while index_s < len(A) and index_r < len(B):
            ch = B[index_r]
            if index_r + 1 < len(B) and B[index_r+1] == '*':
                for i in range(index_s, len(A)+1):
                    if i > index_s and A[i-1] != ch and ch != '.':
                        break
                    if self.isMatch(A, B, i, index_r+2):
                        return 1
                return 0
            else:
                if ch == A[index_s] or ch == '.':
                    index_r += 1
                    index_s += 1
                else:
                    return 0
        if index_s == len(A) and index_r == len(B):
            return 1
        if index_s == len(A) or index_r == len(B):
            return 0
