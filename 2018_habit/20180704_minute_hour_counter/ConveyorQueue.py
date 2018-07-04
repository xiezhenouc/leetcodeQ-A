#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
队列保存每个桶内的事件的数目，以及所有桶内的事件总和
'''

class ConveyorQueue(object):
    # queue
    q = []
    max_items = 0
    # sum of all items in queue q
    total_sum = 0

    def __init__(self, max_items, total_sum = 0):
        self.max_items = max_items
        self.total_sum = total_sum 

    def totalSum(self):
        return self.total_sum

    def shift(self, num_shifted):
        '''
        shift queue
        '''
        # too many shift, just clear queue q
        if(num_shifted > self.max_items):
            self.q = []
            self.total_sum = 0
            return None

        # push 0 to queue end
        while num_shifted > 0:
            self.q.append(0)
            num_shifted -= 1

        # delete front items of queue
        while len(self.q) > self.max_items:
            self.total_sum -= self.q[0]
            self.q.pop()

    def addToBack(self, count):
        if len(self.q) == 0:
            self.shift(1)
        self.q[-1] += count
        self.total_sum += count

if __name__ == '__main__':
    obj = ConveyorQueue(10)
    obj.shift(1)
    obj.addToBack(5)
    obj.shift(1)
    obj.addToBack(4)
    print obj.totalSum()
