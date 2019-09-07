# 感觉吧，这道题的动态规划式子不太好列
# 基本思想是：这次一定偷第i家店铺和这次不偷第i家店中取最大
# 动态规划式子：dp[i] = max(num[i] + dp[i - 2], dp[i - 1])，其中dp[i]表示到第i个房子时能够抢到的最大金额

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])

        dp = [nums[0], max(nums[0], nums[1])]
        for i in range(2, len(nums)):
            cur = max(nums[i] + dp[i - 2], dp[i - 1])
            dp.append(cur)
        return dp[-1]
