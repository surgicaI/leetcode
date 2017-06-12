# https://leetcode.com/problems/elimination-game/#/description

class Solution(object):
    def helper_odd(self, n , dir):
        if n == 3 or n == 1:
            return (n+1)/2
        val = (n-1)/2
        if val%2 == 0:
            ans = self.helper_even(val, self.direcs[dir])
        else:
            ans = self.helper_odd(val, self.direcs[dir])
        return 2 * ans
    
    def helper_even(self, n ,dir):
        if n == 2:
            return 2 if dir == 'left-to-right' else 1
        val = n / 2
        if val % 2 == 0:
            ans = self.helper_even(val, self.direcs[dir])
        else:
            ans = self.helper_odd(val, self.direcs[dir])
        return 2 * ans if dir == 'left-to-right' else (2 * ans) - 1
        
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.direcs = {'left-to-right':'right-to-left', 'right-to-left':'left-to-right'}
        dir = 'left-to-right'
        return self.helper_odd(n, dir) if n%2 else self.helper_even(n, dir)
        