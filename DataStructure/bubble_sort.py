#!/usr/bin/python
# -*- coding: utf-8 -*-

def bubble_sort(alist):
    for j in range(len(alist)-1, 0, -1):
        # j表示每次遍历需要比较的次数，是逐渐减小的
        for i in range(j):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]

li = [54,26,93,17,77]
bubble_sort(li)
print(li)