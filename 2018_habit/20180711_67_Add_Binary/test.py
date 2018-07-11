#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        flag = 0
        i = len(a) - 1
        j = len(b) - 1
        sum_list = []
        while i >= 0 and j >= 0:
            cur = int(a[i]) + int(b[j]) + flag
            num = str(cur % 2)
            flag = cur / 2
            sum_list.insert(0, num)
            i -= 1
            j -= 1

        while i >= 0:
            cur = int(a[i]) + flag
            num = str(cur % 2)
            flag = cur / 2
            sum_list.insert(0, num)
            i -= 1

        while j >= 0:
            cur = int(b[j]) + flag
            num = str(cur % 2)
            flag = cur / 2
            sum_list.insert(0, num)
            j -= 1

        if flag > 0:
            sum_list.insert(0, str(flag))

        return ''.join(sum_list)

obj = Solution()
a = "1010"
b = "1011"
print obj.addBinary(a, b)
