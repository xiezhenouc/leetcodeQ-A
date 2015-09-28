#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Pw @ 2015-09-28 22:13:37

def myMultiple(num):
	result = 1
	i = num 
	while i >= 1:
		result *= i
		i -= 1
	
	return result
	
	return num

def process(mystr):
    k = len(mystr)
    result = []
    index = 0
    i = 0
    count = 0
    for index in range(k):
        i = index 
        count = 0
        while i < k:
            if mystr[i] < mystr[index]:
                count += 1
            i = i + 1
        result.append(count)
        print count
        index += 1
    allsum = 0
    m = 0
    while m < k:
        allsum += result[m] * myMultiple(k-m-1)
        m += 1
    return allsum 
if __name__ == '__main__':
	print process('edcba')
