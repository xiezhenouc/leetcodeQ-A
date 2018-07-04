#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
桶的建立和管理
'''

import time
import ConveyorQueue

class TrailingBucketCounter(object):
    # ConveyorQueue queue
    buckets = None
    # granularity
    secs_per_bucket = 0
    # the last time update() called
    last_update_time = 0

    def __init__(self, num_bucktes, secs_per_bucket):
        self.buckets = ConveyorQueue.ConveyorQueue(num_bucktes)
        self.secs_per_bucket = secs_per_bucket

    def update(self, now):
        current_bucket = now / self.secs_per_bucket
        last_bucket = self.last_update_time / self.secs_per_bucket

        self.buckets.shift(current_bucket - last_bucket)
        self.last_update_time = now

    def add(self, count, now):
        self.update(now)
        self.buckets.addToBack(count)

    def trailingCount(self, now):
        self.update(now)
        return self.buckets.totalSum()

if __name__ == '__main__':
    obj = TrailingBucketCounter(60, 1)
    obj.add(3, time.time())
    obj.add(4, time.time())
    now = time.time()
    print obj.trailingCount(now)
