#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        x_direction = rec1[0] < rec2[2] and rec2[0] < rec1[2]
        y_direction = rec1[1] < rec2[3] and rec2[1] < rec1[3]
 
        return x_direction and y_direction

if __name__ == '__main__':
    obj = Solution()
    rec1 = [0,0,1,1]
    rec2 = [1,0,2,1]
    rec1 = [0,0,2,2] 
    rec2 = [1,1,3,3]
    print obj.isRectangleOverlap(rec1, rec2)
