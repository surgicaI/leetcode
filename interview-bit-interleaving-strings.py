# https://www.interviewbit.com/problems/interleaving-strings/

class Solution:
    # @param A : string
    # @param B : string
    # @param C : string
    # @return an integer
    def __init__(self):
        self.my_map = {}

    def isInterleave(self, s1, s2, s3):
        if len(s1) + len(s2) != len(s3):
            return 0
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        return self.solve(0, 0)

    def solve(self, i, j):
        key = (i,j)
        k = i + j
        if key in self.my_map:
            return self.my_map[key]
        elif i == len(self.s1) and self.s2[j:] == self.s3[k:]:
            result = 1
        elif j == len(self.s2) and self.s1[i:] == self.s3[k:]:
            result = 1
        elif i == len(self.s1) or j == len(self.s2):
            result = 0
        else:
            result = 0
            if self.s1[i] == self.s3[k]:
                result |= self.solve(i+1, j)
            if self.s2[j] == self.s3[k]:
                result |= self.solve(i, j+1)

        self.my_map[key] = result
        return result
