# https://leetcode.com/problems/shuffle-an-array/#/description

class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.nums
        

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        res = copy.copy(self.nums)
        length = len(self.nums)
        for i in range(length):
            rand = random.randrange(i,length)
            res[i], res[rand] =  res[rand], res[i]
        return res
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()