# https://leetcode.com/problems/unique-paths/description/
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[-1 for i in range(n)] for _ in range(m)]
        dp[-1][-1] = 1
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                if dp[i][j] == -1:
                    dp[i][j] = dp[i][j+1] if j+1 < n else 0
                    dp[i][j] += dp[i+1][j] if i+1< m else 0
        return dp[0][0]
