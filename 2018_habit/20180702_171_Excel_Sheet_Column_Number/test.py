#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        mymap = {}

        A_num = ord('A')
        cur_num = A_num
        while cur_num < A_num + 26:
            mymap[chr(cur_num)] = cur_num - A_num + 1
            cur_num += 1

        sum_num = 0
        s_len = len(s)
        for i in range(0, s_len):
            sum_num = (sum_num * 26) + mymap[s[i]]

        return sum_num

if __name__ == '__main__':
    obj = Solution()
    s = 'ZY'
    print obj.titleToNumber(s)
