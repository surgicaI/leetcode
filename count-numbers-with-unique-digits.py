# https://leetcode.com/problems/count-numbers-with-unique-digits/#/description

class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 0:
            return 0
        elif n == 0:
            return 1
        val = num = 9
        for i in range(n-1):
            val *= num
            num -= 1
        return self.countNumbersWithUniqueDigits(n-1) + val