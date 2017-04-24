# https://leetcode.com/problems/word-ladder/#/description
from collections import deque
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordList = set(wordList)
        if endWord not in wordList:
            return 0
        alphabets = list('abcdefghijklmnopqrstuvwxyz')
        myqueue = deque()
        myqueue2 = deque()
        myqueue.append(beginWord)
        level = 2
        while(len(myqueue) > 0):
            word = list(myqueue.pop())
            for i in range(len(word)):
                for a in alphabets:
                    p = word[i]
                    word[i] = a
                    newWord = ''.join(word)
                    if newWord == endWord:
                        return level
                    if newWord in wordList:
                        myqueue2.append(newWord)
                        wordList.remove(newWord)
                    word[i] = p
            if len(myqueue) == 0 and len(myqueue2) != 0:
                myqueue = copy.deepcopy(myqueue2)
                myqueue2.clear()
                level += 1
                    
        return 0