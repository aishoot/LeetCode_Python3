# 最初解法
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter
        times = len(nums) // 2
        dicts = Counter(nums)

        for val in dicts:
            if dicts[val] > times:
                return val


# 一行代码解决问题
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sorted(nums)[len(nums) // 2]