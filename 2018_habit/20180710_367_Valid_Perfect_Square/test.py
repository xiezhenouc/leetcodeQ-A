#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Solution(object):
    def isPerfectSquare1(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True

        i = 0
        j = num / 2 + 1
        while i <= j:
            mid = (i + j) / 2
            if mid * mid < num:
                i = mid + 1
            elif mid * mid > num:
                j = mid - 1
            else:
                return True
        return False
            
    def isPerfectSquare(self, num):
        r = num
        while r * r > num:
            r = (r + num / r) / 2
        return r * r == num

if __name__ == '__main__':
    obj = Solution()
    num = 16
    print obj.isPerfectSquare(num)
