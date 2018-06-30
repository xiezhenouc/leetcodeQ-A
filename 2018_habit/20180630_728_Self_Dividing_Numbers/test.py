#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Solution(object): 
    def coreSDN(self, num):
        ret = False
        if num <= 0:
            return ret
        # remember source num !
        srcnum = num
        while True:
            last_digit = num % 10
            if last_digit == 0:
                return ret
            if srcnum % last_digit != 0:
                return ret
            num /= 10
            if num == 0:
                break
        ret = True
        return ret

    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        retList = []
        start = left 
        while start <= right:
            if self.coreSDN(start):
                retList.append(start)
            start += 1
        return retList
        
if __name__ == '__main__':
    obj1 = Solution()

    left = 1
    right = 22
    print obj1.selfDividingNumbers(left, right)
    # print obj1.coreSDN(21)
