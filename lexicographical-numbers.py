# https://leetcode.com/problems/lexicographical-numbers/#/description

class Solution(object):
    def helper(self, number):
        for n in self.nums:
            if (not n) and (not number):
                continue
            new_number = number*10 + n
            if new_number <= self.max:
                self.result.append(new_number)
                self.helper(new_number)
            else:
                return
            
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        self.max = n
        self.nums = [int(i) for i in list("0123456789")]
        self.result = []
        self.helper(0)
        return self.result
        
        