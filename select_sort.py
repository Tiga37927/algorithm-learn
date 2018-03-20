#!/usr/bin/env python  
# encoding: utf-8  

""" 
@version: v1.0 
@author: young 
@license: Apache Licence  
@contact: 924306667@qq.com 
@site:  
@software: PyCharm 
@file: selectSort.py 
@time: 2018/3/20 10:52 
"""
# 查找最小元素索引
def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

# 选择排序
def selectSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr
print selectSort([5, 3, 6, 2, 10])