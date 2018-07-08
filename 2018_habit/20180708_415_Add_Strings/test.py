#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        len_num1 = len(num1)
        len_num2 = len(num2)

        num_sum = []

        i = len_num1 - 1
        j = len_num2 - 1
        add_flag = 0
        while i >= 0 and j >= 0:
            cur = int(num1[i]) + int(num2[j]) + add_flag
            
            add_flag = cur / 10
            num_sum.insert(0, str(cur % 10))
           
            i -= 1
            j -= 1
        
        while i >= 0:
            cur = int(num1[i]) + add_flag
            
            add_flag = cur / 10
            num_sum.insert(0, str(cur % 10))
           
            i -= 1

        while j >= 0:
            cur = int(num2[j]) + add_flag
            
            add_flag = cur / 10
            num_sum.insert(0, str(cur % 10))
           
            j -= 1
          
        if add_flag > 0:
            num_sum.insert(0, str(add_flag))

        return ''.join(num_sum)

if __name__ == '__main__':
    obj = Solution()
    num1 = '1'
    num2 = '0'
    my_sum = obj.addStrings(num1, num2)
    print my_sum, int(num1) + int(num2)
