# https://www.interviewbit.com/problems/edit-distance/

class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def minDistance(self, A , B):
        self.string1 = A
        self.string2 = B
        self.map = {}
        return self.solve(0,0)

    def solve(self, index1, index2):
        key = (index1, index2)
        if key in self.map:
            return self.map[key]
        if index1 == len(self.string1) or index2 == len(self.string2):
            len1 = len(self.string1) - index1
            len2 = len(self.string2) - index2
            return len1 if len1 else len2
        if self.string1[index1] == self.string2[index2]:
            result = self.solve(index1+1, index2+1)
        else:
            result = min(self.solve(index1+1, index2), self.solve(index1, index2+1))
            result = min(self.solve(index1+1, index2+1), result)
            result += 1
        self.map[key] = result
        return result
s1 = "Anshuman"
s2 = "Antihuman"
s = Solution()
print(s.minDistance(s1, s2))
