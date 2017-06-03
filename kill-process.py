# https://leetcode.com/problems/kill-process/#/description

class Solution(object):
    def killProcess(self, pid, ppid, kill):
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        """
        map = {}
        for child, parent in zip(pid,ppid):
            children = map.get(parent,[])
            children.append(child)
            map[parent] = children
        hit_list = [kill]
        for id in hit_list:
            hit_list.extend(map.get(id,[]))
        return hit_list