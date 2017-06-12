# https://leetcode.com/problems/decode-string/#/description

class Solution(object):
    def process(self):
        res = []
        while self.index < len(self.s) and not self.s[self.index].isdigit():
            res.append(self.s[self.index])
            self.index += 1
        self.index -= 1
        return ''.join(res)

    def helper(self, index):
        if not self.s[self.index].isdigit():
            return self.process()
        res = []
        while self.s[self.index] != '[':
            self.index += 1
        mul = int(''.join(self.s[index:self.index]))
        self.index += 1
        while self.s[self.index] != ']':
            if self.s[self.index].isdigit():
                res.append(self.helper(self.index))
            else:
                res.append(self.s[self.index])
            self.index += 1
        return ''.join(res) * mul

    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        self.s = list(s)
        self.index = 0
        res = []
        while self.index < len(s):
            res.append(self.helper(self.index))
            self.index += 1
        return ''.join(res)
        