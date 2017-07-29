# Given a length n, return the number of strings of length n that can be made up of the letters 'a', 'b', and 'c', where there can only be a maximum of 1 'b's and can only have up to two consecutive 'c's
#
# Example:
# findStrings(3) returns 19
# since the possible combinations are: aaa,aab,aac,aba,abc,aca,acb,baa,bac,bca,caa,cab,cac,cba,cbc,acc,bcc,cca,ccb
# and the invalid combinations are:
# abb,bab,bba,bbb,bbc,bcb,cbb,ccc

class solution:
    def solve(self, n):
        self.result = []
        self.n = n
        self.alphs = list('acb')
        self.helper('')
        # for r in self.result:
        #     print(r)
        return len(self.result)

    def helper(self, partial_str):
        if len(partial_str) == self.n:
            self.result.append(partial_str)
            return
        for c in self.alphs:
            if c == 'b':
                self.alphs.pop()
            if c == 'c' and len(partial_str) >=2 and partial_str[-1] == partial_str[-2] == 'c':
                continue
            self.helper(partial_str+c)
            if c == 'b':
                self.alphs.append('b')

s = solution()
print(s.solve(5))
