# https://leetcode.com/problems/decode-ways/#/description
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        if length == 0 or s[0]=='0':
            return 0
        ways = [0 for _ in s]
        if s[-1] == '0':
            ways[-1] = 0
        else:
            ways[length-1] = 1
        for i in reversed(range(length-1)):
            x = int(s[i])
            y = int(s[i+1])
            if y == 0:
                if 0 < x*10+y <= 26:
                    if i+2 == length:
                        ways[i] = 1
                    else:
                        ways[i] = ways[i+2]
                else:
                    return 0
            else:  
                ways[i] = ways[i+1]
                if x*10+y <= 26:
                    if (i+2) == length:
                        ways[i] += 1
                    else:
                        ways[i] += ways[i+2]
                    
        return ways[0]
