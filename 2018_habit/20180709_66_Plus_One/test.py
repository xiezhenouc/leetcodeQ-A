#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        add_num = 1
        i = len(digits) - 1
        while i >= 0:
           cur = digits[i] + add_num
           
           digits[i] = cur % 10 
           add_num = cur // 10
           
           i -= 1

        if add_num > 0:
            digits.insert(0, add_num)
        return digits 

if __name__ == '__main__':
    obj = Solution()
    digits = [1, 9, 9, 9, 9]
    print obj.plusOne(digits)
