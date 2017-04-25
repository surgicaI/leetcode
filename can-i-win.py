class Solution(object):
    def canPlayerwin(self, nums, desiredTotal):
        hash = str(nums + [desiredTotal])
        if nums[-1] >= desiredTotal:
            self.memo[hash] = True
            return True
        if hash in self.memo:
            return self.memo[hash]
        for i in range(len(nums)):
            if not self.canPlayerwin(nums[:i]+nums[i+1:], desiredTotal-nums[i]):
                self.memo[hash] = True
                return True
        self.memo[hash] = False
        return False
    
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        sum = maxChoosableInteger*(maxChoosableInteger+1)/2
        if sum < desiredTotal:
            return False
        elif sum == desiredTotal:
            return maxChoosableInteger%2 != 0
        self.memo = {}
        nums = list(range(1,maxChoosableInteger+1))
        return self.canPlayerwin(nums, desiredTotal)
