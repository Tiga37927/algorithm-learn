#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: young 
@license: Apache Licence  
@contact: 924306667@qq.com 
@site:  
@software: PyCharm 
@file: quick_sort.py 
@time: 2018/3/20 13:43 
"""
"""
每一层需要时间O(n)
高度O(log(n))
复杂度O(n log(n))
"""

def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)
print quicksort([10, 5, 2, 3])