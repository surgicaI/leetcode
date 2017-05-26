# https://leetcode.com/problems/complex-number-multiplication/#/description

class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        real_a, non_real_a = a.split('+')
        real_a = int(real_a)
        non_real_a = int(non_real_a.strip('i'))
        real_b, non_real_b = b.split('+')
        real_b = int(real_b)
        non_real_b = int(non_real_b.strip('i'))
        
        real_c = (real_a * real_b) - (non_real_a * non_real_b)
        non_real_c = (non_real_a * real_b) + (real_a * non_real_b)
        
        return str(real_c) + '+' + str(non_real_c) + 'i'