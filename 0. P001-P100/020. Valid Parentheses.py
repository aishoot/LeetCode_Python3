#!/usr/bin/python
# -*- coding: utf-8 -*-

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack, dicts = [], {'(': ')', ')': '(', '{': '}', '}': '{', '[': ']', ']': '['}

        for ss in s:
            if len(stack) == 0:
                stack.append(ss)
            else:
                stack.pop() if dicts[ss] == stack[-1] else stack.append(ss)

        return True if len(stack) == 0 else False
