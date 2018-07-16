#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = 1
        if x < 0:
            flag = -1
            x = 0 - x
        result = 0
        while x > 0:
            result = result * 10 + x % 10
            x = x / 10
        ret = flag * result
        if ret < 0 - 2 ** 31 or ret > 2 ** 31 - 1:
            return 0
        return ret

obj = Solution()
x_list = [0 - 2 ** 31 - 1, 0 - 2 ** 31, 0 - 2 ** 31 + 1, -12, -9, -1, 0, 1, 123, 2 ** 31 - 1, 2 ** 31]
for x in x_list:
    print x, obj.reverse(x)


        

