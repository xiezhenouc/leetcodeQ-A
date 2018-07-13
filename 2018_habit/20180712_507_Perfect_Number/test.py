#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math


class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 1:
            return False
        factor_set = set()
        factor_set.add(1)

        factor_bound = int(math.sqrt(num)) + 1
        for i in range(2, factor_bound + 1):
            if num % i == 0:
                factor_set.add(i)
                factor_set.add(num / i)

        return sum(factor_set) == num


obj = Solution()
num = 100000000
print obj.checkPerfectNumber(num)

# for num in range(0, 100000):
#    if obj.checkPerfectNumber(num):
#        print num
#
