# https://www.interviewbit.com/problems/word-break/

class Solution:
    # @param A : string
    # @param B : list of strings
    # @return an integer
    def wordBreak(self, A, B):
        self.string = A
        self.dict = set(B)
        self.length = len(A)
        self.my_map = {}
        self.lengths = [len(i) for i in B]
        for i in range(len(A)-1, -1, -1):
            self.solve(i)
        return self.my_map[0]

    def solve(self, start_index):
        if start_index in self.my_map:
            return self.my_map[start_index]
        for length in self.lengths:
            if start_index + length > self.length:
                continue
            word = self.string[start_index:start_index+length]
            if start_index + length == self.length and word in self.dict:
                self.my_map[start_index] = 1
                return 1
            elif start_index + length < self.length:
                if word in self.dict and self.solve(start_index+length):
                    self.my_map[start_index] = 1
                    return 1
        self.my_map[start_index] = 0
        return 0
