# 解法1-优化版本
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach, n = 0, len(nums)
        for i, x in enumerate(nums):
            if max_reach < i:
                return False
            if max_reach >= n - 1:
                return True
            max_reach = max(max_reach, i + x)


# 解法2-逆序判断
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        idx = len(nums)-1
        for i in range(len(nums)-2, -1, -1):
            if idx-i <= nums[i]:  # 能够到达
                idx = i
        return idx == 0
