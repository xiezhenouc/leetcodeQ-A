#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 位数
        digit = 1
        ith = 1
        # 进制
        base = 9
        while n > digit * base:
            n -= digit * base
            ith += base
            digit += 1
            base *= 10

        return int(str(ith + (n-1) / digit)[(n-1) % digit])

obj = Solution()
n_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 150, 151]
for n in n_list:
    print n, obj.findNthDigit(n)
        


