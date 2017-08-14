# https://leetcode.com/problems/remove-duplicate-letters/description/
class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        my_map = {}
        out = []
        for index, ch in enumerate(s):
            l = my_map.get(ch, [])
            l.append(index)
            my_map[ch] = l
        chars = collections.deque(sorted(my_map.keys()))
        min_pos = -1
        while chars:
            for ch in chars:
                index = 0
                while my_map[ch][index] < min_pos:
                    index += 1
                pos = my_map[ch][index]
                for i in range(pos):
                    c = s[i]
                    if c in my_map and my_map[c][-1] < pos:
                        break
                else:
                    out.append(ch)
                    my_map.pop(ch)
                    chars.remove(ch)
                    min_pos = pos
                    break
        return ''.join(out)
