# https://leetcode.com/problems/add-and-search-word-data-structure-design/#/description
class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        ptr = self.root
        for c in word:
            if c in ptr:
                ptr = ptr[c]
            else:
                ptr[c] = {}
                ptr = ptr[c]
        ptr[None] = None

    def search(self, word, ptr = None):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        
        if not ptr:
            ptr = self.root
        for i in range(len(word)):
            if word[i] == '.':
                ans = False
                for key,val in ptr.items():
                    if key == None:
                        continue
                    temp = self.search(word[i+1:],ptr[key])
                    ans = ans or temp
                    if ans:
                        print key
                        break
                return ans
            elif not word[i] in ptr:
                return False
            ptr = ptr[word[i]]
        if None in ptr:
            return True
        else:
            return False
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)