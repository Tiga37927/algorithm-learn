#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: young 
@license: Apache Licence  
@contact: 924306667@qq.com 
@site:  
@software: PyCharm 
@file: divide_conquer.py 
@time: 2018/3/20 11:18 
"""
# 分治策略（eg:快排）
"""
原理：
1.找出简单的基线条件
2.确定如何缩小问题的规模，使其符合基线条件
"""
def suma(arr):
    if(len(arr) == 1):
        return arr[0]
    return arr[0]+suma(arr.__getslice__(1, len(arr)))
print suma([1,1])