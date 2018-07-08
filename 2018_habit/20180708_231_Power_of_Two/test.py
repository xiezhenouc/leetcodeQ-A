#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        return not (n & (n - 1))

if __name__ == '__main__':
    obj = Solution()
    n = 256
    n = 218
    print obj.isPowerOfTwo(n)
