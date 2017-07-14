# https://leetcode.com/problems/longest-absolute-file-path/#/description

class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        stack = []
        input = input.split('\n')
        current_tabs = 0
        max_string_length = 0
        current_string_length = 0
        for name in input:
            tabs = name.count('\t')
            if tabs <= current_tabs:
                while len(stack) > tabs:
                    elem = stack.pop()
                    current_string_length -= (len(elem) + 1)
            current_tabs = tabs
            name_strip = name.strip('\t')
            stack.append(name_strip)
            current_string_length += (len(name_strip) + 1)
            if '.' in name and (current_string_length - 1) > max_string_length:
                max_string_length = current_string_length - 1
        return max_string_length
