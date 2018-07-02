#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Solution(object):
    single_map = {
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000
    }
    
    double_map = {
        'IV' : 4,
        'IX' : 9,
        'XL' : 40,
        'XC' : 90,
        'CD' : 400,
        'CM' : 900
    }

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_len = len(s)
        ret = 0
        i = 0
        while i < s_len:
            if i < s_len - 1 and self.double_map.has_key(s[i] + s[i+1]):
                ret += self.double_map[s[i] + s[i+1]]
                i += 2
                continue
            ret += self.single_map[s[i]]
            i += 1
        return ret                    

if __name__ == '__main__':
    obj = Solution()
    s = 'MCMXCIV'
    print obj.romanToInt(s)
