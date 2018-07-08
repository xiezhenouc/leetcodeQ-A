#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Solution(object):
    def calc(self, num):
        ret = 0

        while num > 0:
            ret += (num % 10) ** 2
            num = num // 10

        return ret

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = set()

        while n not in seen:
            seen.add(n)
            n = self.calc(n)

        return n == 1
        
if __name__ == '__main__':
    obj = Solution()
    n = 19
    n = 28
    # n = 29
    # n = 13
    print n
    print obj.isHappy(n)
