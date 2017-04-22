#https://leetcode.com/problems/simplify-path/#/description
from collections import deque
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path = list(path)
        stack = deque()
        while len(path)>0:
            if '/' in path:
                i = path.index('/')
            else :
                i= -1
            if i==0 :
                path.remove('/')
            elif i>0 :
                stack.append(''.join(path[0:i]))
                path = path[i+1:]
            else :
                stack.append(''.join(path))
                path = []
        path = ['/']
        while len(stack)>0:
            x = stack.popleft()
            if x!='.' and x!='..':
                path.append(x)
                path.append('/')
            elif x == '..' and len(path)>1:
                path = path[:-2]
        if len(path)>1:
            return ''.join(path[:-1])
        else:
            return ''.join(path)
        