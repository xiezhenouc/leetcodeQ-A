#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

class Solution(object):
    def sum1ton(self, n):
        return (1 + n) * n / 2

    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        end = int((math.sqrt(1 + 8 * n) - 1) / 2) + 1
        start = (math.sqrt(1 + 8 * n) - 3) / 2

        while True:
            left = self.sum1ton(end)
            right = self.sum1ton(end + 1)
            if left <= n and n < right:
                return end
            if left > n:
                end -= 1

obj = Solution()
n = 187000000
print obj.arrangeCoins(n)
print n
print obj.sum1ton(19338)
print obj.sum1ton(19339)
