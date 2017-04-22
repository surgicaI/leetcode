# https://leetcode.com/problems/single-element-in-a-sorted-array/#/description
from collections import deque
class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        genes = ['A','C','G','T']
        mybank = set()
        for s in bank:
            mybank.add(s)
            
        myqueue = deque()
        myqueue.append(start)
        level = 0
        myqueue2 = deque()
        while len(myqueue)>0:
            curr = myqueue.popleft()
            if curr == end:
                return level
            curr = list(curr)
            for i in range(len(curr)):
                for gene in genes:
                    prev = curr[i]
                    curr[i] = gene
                    curr_string = ''.join(curr)
                    if curr_string in bank:
                        bank.remove(curr_string)
                        myqueue2.append(curr_string)
                    curr[i] = prev
            if len(myqueue)==0 and len(myqueue2)!=0:
                myqueue = copy.deepcopy(myqueue2)
                myqueue2.clear()
                level += 1
                
        return -1 
            