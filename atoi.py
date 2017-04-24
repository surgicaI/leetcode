# https://leetcode.com/problems/string-to-integer-atoi/#/description

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        result = 0
        is_negetive = 1
        digits = list('0123456789')
        digit_set = set(digits)
        str = list(str.strip())
        index = 0
        for c in str:
            if c in digit_set:
                result = (result * 10) + digits.index(c)
            elif index==0 and (c == '+' or c == '-'):
                if c == '-':
                    is_negetive = -1
            else:
                break
            index += 1
        result = result*is_negetive
        if result > 2147483647:
            result = 2147483647
        elif result < -2147483648:
            result = -2147483648
        
        return result
            