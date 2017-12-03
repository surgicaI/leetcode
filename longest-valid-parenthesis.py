# https://leetcode.com/problems/longest-valid-parentheses/description/
class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        minVal = -1
        res = 0
        stack = []
        for index , ch in enumerate(s):
            if ch == '(':
                stack.append(index)
            elif ch == ')':
                if stack:
                    stack.pop()
                    if stack:
                        res = max(res, index - stack[-1])
                    else:
                        res = max(res, index - minVal)
                else:
                    minVal = index
        return res
