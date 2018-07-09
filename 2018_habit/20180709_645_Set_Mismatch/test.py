#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        unique_nums_set = set(nums)
        all_nums_set = set()
        for i in range(n):
            all_nums_set.add(i+1)

        duplicate = sum(nums) - sum(unique_nums_set)
        missing = all_nums_set - unique_nums_set

        return [duplicate, missing.pop()]
        

if __name__ == '__main__':
    obj = Solution()
    nums = [4,2,2,1]
    print obj.findErrorNums(nums)
