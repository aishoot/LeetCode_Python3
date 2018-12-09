#!/usr/bin/python
# -*- coding: utf-8 -*-

def selection_sort(alist):
    n = len(alist)
    for i in range(n-1):  # 需要进行n-1次选择操作
        min_index = i  # 记录最小位置
        for j in range(i+1, n):  # 从i+1位置到末尾选择出最小数据
            if alist[j] < alist[min_index]:
                min_index = j
        if min_index != i:  # 如果选择出的数据不在正确位置，进行交换
            alist[i], alist[min_index] = alist[min_index], alist[i]

alist = [54,226,93,17,77]
selection_sort(alist)
print(alist)