#!/usr/bin/python
# -*- coding: utf-8 -*-

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_map = {}
        for index, num in enumerate(nums):
            if target - num in hash_map:
                return [hash_map[target - num], index]
            else:
                hash_map[num] = index