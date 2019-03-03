#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        return os.path.commonprefix(strs)
