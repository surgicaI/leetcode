# https://www.interviewbit.com/problems/distinct-subsequences/

class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def __init__(self):
        self.my_map = {}

    def numDistinct(self, string1, string2, i=0, j=0):
        if j == len(string2):
            return 1
        if i == len(string1):
            return 0
        key = (i,j)
        if key in self.my_map:
            return self.my_map[key]
        if string1[i] == string2[j]:
            self.my_map[key] = self.numDistinct(string1, string2, i+1, j+1) + self.numDistinct(string1, string2, i+1, j)
            return self.my_map[key]
        else:
            self.my_map[key] = self.numDistinct(string1, string2, i+1, j)
            return self.my_map[key]
