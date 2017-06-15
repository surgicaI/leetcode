# https://leetcode.com/problems/flatten-nested-list-iterator/#/description

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
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

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        index = 0
        item = [nestedList, index]
        self.stack = [item] if len(nestedList) else []
        self.helper()
        
    def helper(self):
        if not self.stack:
            self.nextVal = None
            return
        list, index = self.stack[-1]
        item = list[index]
        index += 1
        if index < len(list):
            self.stack[-1][-1] = index
        else:
            self.stack.pop()
        if item.isInteger():
            self.nextVal = item.getInteger()
        else:
            list = item.getList()
            if list:
                self.stack.append([item.getList(), 0])
            self.helper()

    def next(self):
        """
        :rtype: int
        """
        val = self.nextVal
        self.helper()
        return val
        
    def hasNext(self):
        """
        :rtype: bool
        """
        return True if self.nextVal != None else False
        

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())