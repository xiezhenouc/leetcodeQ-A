#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        five_count = 0
        while n > 0:
            n = n / 5 
            five_count += n
        return five_count

obj = Solution()
print obj.trailingZeroes(100)
