# My Solution
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        from collections import Counter
        dicts = Counter(nums)
        set1 = set(dicts.keys())
        return set(range(1, len(nums) + 1)) - set1

# 继续优化
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        return list(set(range(1,len(nums) + 1)) - set(nums))
