# https://leetcode.com/problems/generate-parentheses/#/description
class Solution(object):
    def __init__(self):
        self.dict = {}
        self.dict[0] = ['']
        self.dict[1] = ['()']
        
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n in self.dict:
            return self.dict[n]
        result = []
        for i in range(n):
            temp_res_1 = self.generateParenthesis(i)
            temp_res_2 = self.generateParenthesis(n-i-1)
            for t1 in temp_res_1:
                for t2 in temp_res_2:
                    combine = "(" + t2 + ")" + t1
                    result.append(combine)
        self.dict[n] = result
        return result