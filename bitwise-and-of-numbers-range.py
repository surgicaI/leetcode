# https://leetcode.com/problems/bitwise-and-of-numbers-range/description/
class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m.bit_length() != n.bit_length():
            return 0
        else:
            m = bin(m)
            n = bin(n)
            result = []
            for index, (mi, ni) in enumerate(zip(m,n)):
                if mi == ni:
                    result.append(mi)
                else:
                    result.extend(['0' for _ in m[index:]])
                    break
            result = int(''.join(result), 2)
            return result
