#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_len = len(nums)
        min_nums = nums[0]
        for i in range(nums_len):
            min_nums = min(min_nums, nums[i])

        move_count = 0
        for i in range(nums_len):
            move_count += (nums[i] - min_nums)

        return move_count

            
if __name__ == '__main__':
    obj = Solution()
    nums = [1, 2311111]
    print obj.minMoves(nums)
