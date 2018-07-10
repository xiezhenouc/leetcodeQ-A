#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if x == 0:
            return True 
        
        x_src = x
        x_copy = 0 
        while x > 0:
            x_copy = (x_copy * 10 + x % 10)
            x /= 10
        return x_src == x_copy

if __name__ == '__main__':
    obj = Solution()
    x = 121
    print obj.isPalindrome(x)
