#!/usr/bin/python
# -*- coding: utf-8 -*-

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = -1 if x < 0 else 1
        num = s * int(str(abs(x))[::-1])
        if (num > 2 ** 31 - 1) or (num < -2 ** 31):
            return 0
        else:
            return num