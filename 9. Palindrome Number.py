#!/usr/bin/python
# -*- coding: utf-8 -*-

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return True if str(x)[::-1] == str(x) else False