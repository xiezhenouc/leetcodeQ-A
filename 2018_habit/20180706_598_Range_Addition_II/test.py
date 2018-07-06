#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    MAX_RANGE = 1000000

    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        if len(ops) < 1:
            return m * n

        max_range_maximum_row = self.MAX_RANGE
        max_range_maximum_col = self.MAX_RANGE
        for range_tuple in ops:
            a = range_tuple[0]
            b = range_tuple[1]

            max_range_maximum_row = min(max_range_maximum_row, a)
            max_range_maximum_col = min(max_range_maximum_col, b)
        
        return max_range_maximum_row * max_range_maximum_col

if __name__ == '__main__':
    obj = Solution()
    m = 3
    n = 3
    operations = [[2,2],[3,3]]
    m = 18
    n = 3
    operations = [[16,1],[14,3],[14,2],[4,1],[10,1],[11,1],[8,3],[16,2],[13,1],[8,3],[2,2],[9,1],[3,1],[2,2],[6,3]]

    print obj.maxCount(m, n, operations)
