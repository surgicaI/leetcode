# https://leetcode.com/problems/magical-string/#/description

class Solution(object):
    def magicalString(self, n):
        """
        :type n: int
        :rtype: int
        """
        dict = {'1':'2', '2':'1'}
        magical_string = list('122') 
        answer = min(1,n)
        for i in range(2,n):
            if magical_string[i] == '1':
                res = [dict[magical_string[-1]]]
                answer += 1
            else:
                res = [dict[magical_string[-1]]] * 2
            magical_string.extend(res)
        return answer