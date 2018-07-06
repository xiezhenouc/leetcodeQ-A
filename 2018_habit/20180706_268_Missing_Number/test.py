#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_sum = sum(nums)

        total_nums = len(nums) + 1
        max_nums = len(nums)
        total_sum = total_nums * max_nums * 0.5

        return int(total_sum - nums_sum)

if __name__ == '__main__':
    obj = Solution()
    nums = [9,6,4,2,3,5,7,0,1]
    print obj.missingNumber(nums)
