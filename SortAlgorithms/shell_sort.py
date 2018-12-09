#!/usr/bin/python
# -*- coding: utf-8 -*-

def shell_sort(alist):
    n = len(alist)
    gap = n // 2  # 初始步长

    while gap > 0:
        for i in range(gap, n):  # 按步长进行插入排序
            j = i
            # 插入排序
            while j>=gap and alist[j-gap] > alist[j]:
                alist[j-gap], alist[j] = alist[j], alist[j-gap]
                j -= gap
        gap = gap // 2  # 得到新的步长

alist = [54,26,93,17,77,31,44,55,20]
shell_sort(alist)
print(alist)