#!/usr/bin/python
# -*- coding: utf-8 -*-

class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = 0
        prev = 0

        for i in s:
            curr = map[i]
            if prev < curr:
                res = res + (curr - 2 * prev)
            else:
                res = res + curr
            prev = curr

        return res
