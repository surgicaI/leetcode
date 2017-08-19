# https://www.interviewbit.com/problems/min-jumps-array/

class Solution:
    # @param A : list of integers
    # @return an integer
    def jump_dp_solution(self, jumps_array):
        length = len(jumps_array)
        min_jumps = [-1] * length
        min_jumps[-1] = 0
        for index, max_jump in enumerate(reversed(jumps_array)):
            index = length - index -1
            if min_jumps[index] != -1:
                continue
            result = None
            for jump in range(max_jump):
                jump_index = index + jump + 1
                if jump_index < length and min_jumps[jump_index] != -1:
                    temp = min_jumps[jump_index] + 1
                    result = min(result, temp) if result else temp

            min_jumps[index] = result if result else -1
        return min_jumps[0]

    # greedy algorithm
    def jump(self, jumps_array):
        index = 0
        jumps = 0
        length = len(jumps_array)
        if length < 2:
            return 0
        while index < length:
            if jumps_array[index] == 0:
                return -1
            max_reachable = index + jumps_array[index]
            jumps += 1
            if max_reachable >= length -1:
                return jumps
            temp = -1
            for i in range(index+1, max_reachable+1):
                if i + jumps_array[i] > temp:
                    temp = i + jumps_array[i]
                    index = i

A = [ 33, 21, 50, 0, 0, 46, 34, 3, 0, 12, 33, 0, 31, 37, 15, 17, 34, 18, 0, 4, 12, 41, 18, 35, 37, 34, 0, 47, 0, 39, 32, 49, 5, 41, 46, 26, 0, 2, 49, 35, 4, 19, 2, 27, 23, 49, 19, 38, 0, 33, 47, 1, 21, 36, 18, 33, 0, 1, 0, 39, 0, 22, 0, 9, 36, 45, 31, 4, 14, 48, 2, 33, 0, 39, 0, 37, 48, 44, 0, 11, 24, 16, 10, 23, 22, 41, 32, 14, 22, 16, 23, 38, 42, 16, 15, 0, 39, 23, 0, 42, 15, 25, 0, 41, 2, 48, 28 ]
x = Solution()
print(x.jump(A))
