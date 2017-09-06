# https://www.interviewbit.com/problems/n3-repeat-number/

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        dict = {}
        for n in A:
            if n in dict:
                dict[n] += 1
            else:
                dict[n] = 1
            if len(dict.items()) == 3:
                self.remove(dict)
        for n in dict.keys():
            if self.test(n, A):
                return n
        return -1

    def remove(self, d):
        for n in d.keys():
            val = d[n] - 1
            if val > 0:
                d[n] = val
            else:
                d.pop(n)

    def test(self, n, A):
        count = 0
        for i in A:
            if i == n:
                count += 1
        if count > len(A)/3:
            return True
        return False
