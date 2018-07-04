#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
实现分钟小时计数器
'''

import time
import TrailingBucketCounter

class MinuteHourCounter(object):
    minute_counts = None
    hour_counts = None

    def __init__(self):
        # TrailingBucketCounter(buckets, secs_per_bucket)
        self.minute_counts = TrailingBucketCounter.TrailingBucketCounter(60, 1)
        self.hour_counts = TrailingBucketCounter.TrailingBucketCounter(60, 60)

    def add(self, count):
        now = time.time()
        self.minute_counts.add(count, now)
        self.hour_counts.add(count, now)

    def minuteCount(self):
        now = time.time()
        return self.minute_counts.trailingCount(now)

    def hourCount(self):
        now = time.time()
        return self.hour_counts.trailingCount(now)

if __name__ == '__main__':
    obj = MinuteHourCounter()
    add_count_num  = 100
    for i in range(add_count_num):
        obj.add(i)

    print obj.minuteCount()
    print obj.hourCount()
