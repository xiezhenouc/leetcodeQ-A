#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Solution(object):
    def isArithmetic(self, arr, i, j, k):
        return arr[k] - arr[j] == arr[j] - arr[i]

    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        if n <= 2:
             return 0
        x = [0] * n
        ret = 0
        if self.isArithmetic(A, 0, 1, 2):
            x[2] = 1
            ret += x[2]
        i = 3
        while i < n:
            if self.isArithmetic(A, i-2, i-1, i):
                x[i] = x[i-1] + 1
            ret += x[i]
            i += 1
        print x
        return ret
             
obj = Solution()
A = [1, 2, 3, 4]
print A
print obj.numberOfArithmeticSlices(A)
