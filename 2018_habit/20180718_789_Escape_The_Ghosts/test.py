#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Solution(object):
    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        target_len = abs(target[0]) + abs(target[1])

        for i, j in ghosts:
            ghosts_len = abs(i - target[0]) + abs(j - target[1])
            if ghosts_len <= target_len:
                return False
        return True

obj = Solution()
ghosts = [[1, 0], [0, 3]]
target = [0, 1]
print obj.escapeGhosts(ghosts, target)

ghosts = [[1, 0]]
target = [2, 0]
print obj.escapeGhosts(ghosts, target)

ghosts = [[2, 0]]
target = [1, 0]
print obj.escapeGhosts(ghosts, target)
