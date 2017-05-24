# https://leetcode.com/problems/divide-two-integers/#/description

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        MAX_INT = 2**31 - 1
        MIN_INT = -1 * MAX_INT - 1 
        if divisor == 0 or (dividend == MIN_INT and divisor == -1):
            return MAX_INT
        answer = 0
        sign = 1 if dividend*divisor >= 0 else -1
        dividend = abs(dividend)
        divisor = abs(divisor)
        while dividend >= divisor:
            temp = divisor
            index = 0
            while dividend >= (temp<<1):
                temp = temp << 1
                index += 1
            dividend -= temp
            answer += 1 << index
        return answer*sign