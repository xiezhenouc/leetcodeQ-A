#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

class Solution(object):
    def swap(self, my_list, i, j):
        my_list[i], my_list[j] = my_list[j], my_list[i]

    def smallerIndexFromChilds(self, min_heap, i, lchild, rchild):
        n = len(min_heap)
        if lchild >= n:
            return i
        if rchild >= n:
            return lchild

        if min_heap[lchild] < min_heap[rchild]:
            return lchild
        else:
            return rchild

    def updateMinHeap(self, min_heap):
        i = 0
        n = len(min_heap)

        while i < n:
            left = 2 * i + 1
            right = 2 * i + 2

            small = self.smallerIndexFromChilds(min_heap, i, left, right)
            if min_heap[small] >= min_heap[i]:
                break
            self.swap(min_heap, i, small)
            i = small

    def maximumProductMinHeap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MIN_NUM = 0 - sys.maxint
        HEAP_SIZE = 3
        min_heap = []
        for i in range(HEAP_SIZE):
            min_heap.append(MIN_NUM) 

        for num in nums:
            if num > min_heap[0]:
                min_heap[0] = num
                self.updateMinHeap(min_heap)

        max_prod = 1
        for num in min_heap:
            max_prod *= num

        return max_prod

    def biggerIndexFromChilds(self, max_heap, i, lchild, rchild):
        n = len(max_heap)
        if lchild >= n:
            return i
        if rchild >= n:
            return lchild

        if max_heap[lchild] < max_heap[rchild]:
            return rchild
        else:
            return lchild

    def updateMaxHeap(self, max_heap):
        i = 0
        n = len(max_heap)

        while i < n:
            left = 2 * i + 1
            right = 2 * i + 2

            big = self.biggerIndexFromChilds(max_heap, i, left, right)
            if max_heap[big] <= max_heap[i]:
                break
            self.swap(max_heap, i, big)
            i = big

    def maximumProductMaxHeap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MAX_NUM = sys.maxint
        HEAP_SIZE = 2
        max_heap = []
        for i in range(HEAP_SIZE):
            max_heap.append(MAX_NUM) 

        for num in nums:
            if num < max_heap[0]:
                max_heap[0] = num
                self.updateMaxHeap(max_heap)

        max_nums = max(nums)
        max_prod = 1
        for num in max_heap:
            max_prod *= num

        return max_prod * max_nums

    def maximumProduct(self, nums):
        return max(self.maximumProductMaxHeap(nums), self.maximumProductMinHeap(nums))

       
if __name__ == '__main__':
    obj = Solution()
    nums = [1,2,3,4]
    nums = [1,2,3]
    nums = [-4,-3,-2,-1,60]
    print obj.maximumProduct(nums)
