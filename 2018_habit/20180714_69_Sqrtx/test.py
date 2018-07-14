#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <= 0:
             return 0
        if x == 1:
             return 1

        i = 1
        j = x / 2 + 1
        mid = (i + j) / 2
        # ! 注意边界前面是>= 后面是<
        while not (mid ** 2 <= x and (mid + 1) ** 2 > x):
            if mid ** 2 > x:
                j = mid
            if (mid + 1) ** 2 <= x:
                i = mid + 1
            mid = (i + j) / 2
        return mid

obj = Solution()
x_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 100, 101]
for x in x_list:
    print x, obj.mySqrt(x)

for x in range(1, 100):
    print x, obj.mySqrt(x)
