#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        if c < 0:
            return False

        max_bound = int(c ** 0.5) + 1 
        for a in range(0, max_bound + 1):
            b = c - a * a
            if b >= 0 and int(b ** 0.5) ** 2 == b:
                return True
        return False
        

obj = Solution()
for c in range(0, 100):
    if obj.judgeSquareSum(c):
        print c
