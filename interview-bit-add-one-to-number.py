# https://www.interviewbit.com/problems/add-one-to-number/

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        result = []
        if not A:
            return result
        carry = 1
        index = 0
        while index < len(A) and A[index] == 0:
            index += 1
        for i in reversed(A[index:]):
            n = i + carry
            carry = n / 10
            result.append(n%10)
        if carry != 0:
            result.append(carry)
        return list(reversed(result))
