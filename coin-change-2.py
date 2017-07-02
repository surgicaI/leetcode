class Solution(object):
    def __init__(self):
        self.table = None

    def change(self, amount, coins ,index=0):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """

        if amount == 0:
            return 1
        elif amount < 0:
            return 0

        if self.table == None :
            self.table = [[-1 for i in range(amount)] for j in range(len(coins))]

        if self.table[index][amount-1]!=-1:
            return self.table[index][amount-1]


        result = 0
        for i in range(index,len(coins)):
            result += self.change(amount-coins[i],coins,i)

        self.table[index][amount-1] = result

        return result