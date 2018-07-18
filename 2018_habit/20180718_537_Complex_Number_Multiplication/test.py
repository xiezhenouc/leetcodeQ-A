#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a1 = int(a.split('+')[0])
        a2 = int(a.split('+')[1].split('i')[0])

        b1 = int(b.split('+')[0])
        b2 = int(b.split('+')[1].split('i')[0])

        c1 = (a1 * b1 - a2 * b2)
        c2 = (a1 * b2 + a2 * b1)

        return str(c1) + '+' + str(c2) + 'i'
        

a = '1+-1i'
b = '1+-1i'
obj = Solution()
print obj.complexNumberMultiply(a, b)
