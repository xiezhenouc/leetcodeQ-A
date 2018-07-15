#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        title_str = []
        while n > 0:
            cur = n % 26
            if cur == 0:
                cur = 26
            digit = (cur + ord('A') - 1)
            n -= cur
            n /= 26
           
            title_str.insert(0, chr(digit))
        return ''.join(title_str)

obj = Solution()
for n in range(1, 58):
    print n, obj.convertToTitle(n)
print obj.convertToTitle(701)

        
