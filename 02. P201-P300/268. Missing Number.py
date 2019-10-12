# 一行代码解决问题
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return (set(range(len(nums) + 1)) - set(nums)).pop()

# 或者解法2
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return int((0 + n) * (n + 1) / 2) - sum(nums)

