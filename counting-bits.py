# https://leetcode.com/problems/counting-bits/#/description

class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        result = [0]
        prev_mul = 0
        next_mul = 1
        for i in range(1,num+1):
            if i < next_mul:
                result.append(1+result[i-prev_mul])
            else:
                result.append(1)
                prev_mul = next_mul
                next_mul *= 2
        return result
