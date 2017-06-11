# https://leetcode.com/problems/reconstruct-original-digits-from-english/#/description

import collections
class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        nums = list('0123456789')
        res = collections.Counter()
        dict = collections.Counter()
        for ch in s:
            dict[ch] += 1
        # zero
        res['0'] = dict['z']
        dict['o'] -= dict['z']
        res['2'] = dict['w']
        dict['t'] -= dict['w']
        dict['o'] -= dict['w']
        res['4'] = dict['u']
        dict['f'] -= dict['u']
        dict['o'] -= dict['u']
        res['6'] = dict['x']
        dict['s'] -= dict['x']
        dict['i'] -= dict['x']
        res['8'] = dict['g']
        dict['i'] -= dict['g']
        dict['t'] -= dict['g']
        res['1'] = dict['o']
        res['3'] = dict['t']
        res['5'] = dict['f']
        dict['i'] -= dict['f']
        res['7'] = dict['s']
        res['9'] = dict['i']
        
        ans = ''
        for n in nums:
            ans += n*res[n]
        return ans
        