# https://leetcode.com/problems/mini-parser/#/description

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution(object):
    def helper(self, s, index):
        i = index
        result = []
        temp_int = []
        while i < len(s):
            char = s[i]
            if char == '[':
                temp_res, i = self.helper(s,i+1)
                result.append(temp_res)
            elif char == ']':
                if len(temp_int) > 0:
                    result.append(NestedInteger(int(''.join(temp_int))))
                return result, i
            elif char == ',':
                if len(temp_int) > 0:
                    result.append(NestedInteger(int(''.join(temp_int))))
                temp_int = []
            else:
                temp_int.append(char)
            i += 1
                
        
    def deserialize(self, s):
        """
        :type s: str
        :rtype: NestedInteger
        """
        if len(s) > 0:
            if s[0] == '[':
                res, i = self.helper(s,1)
            else:
                res = NestedInteger(int(s))
            return res
        