#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Pw @ 2015-09-28 22:13:37

'''
input a string , output it's position (by dictionary)
example:
    abcde 0
    abced 1
    ...
    edcab 118
    edcba 119

core thought:
    xn * (n-1)! + xn-1 * (n-2)! + ... + x2 * 1! + x1 * 0!
    xi : the count of elements lower than xi and after xi 
'''

def myMultiple(num):
    'return num!'
    result = 1
    i = num 
    while i >= 1:
        result *= i
        i -= 1
    
    return result

def process(mystr):
    'get position by dictionary'
    k = len(mystr)
    result = []
    index = 0
    i = 0

    #get coef 
    while index < k:
        i = index 
        count = 0
        while i < k:
            if mystr[i] < mystr[index]:
                count += 1
            i = i + 1
        result.append(count)
        index += 1

    #final calc
    allsum = 0
    m = 0
    while m < k:
        allsum += result[m] * myMultiple(k-m-1)
        m += 1

    return allsum 

if __name__ == '__main__':
	print process('edcba')
