# 我的代码-2192 ms, faster than 5.05% of Python3
class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        summary = 0
        for ii in range(1, len(height)-1):
            level = min(max(height[:ii]), max(height[-(len(height)-ii-1):]))
            if level > height[ii]:
                summary = level - height[ii] + summary
        return summary

# 我的代码2-优化版-48 ms, faster than 74.32% of Python3
"""
基于动态规划Dynamic Programming的，我们维护一个一维的dp数组，这个DP算法需要遍历两遍数组，
第一遍遍历dp[i]中存入i位置左边的最大值，然后开始第二遍遍历数组，第二次遍历时找右边最大值，
然后和左边最大值比较取其中的较小值，然后跟当前值A[i]相比，如果大于当前值，则将差值存入结果
"""
class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        summary = 0
        dp = [0] * len(height)
        max_left, dp[1] = height[0], height[0]

        for ii in range(2, len(height) - 1):
            if height[ii - 1] > max_left:
                max_left = height[ii - 1]
            dp[ii] = max_left

        max_right = height[-1]
        for jj in range(-2, -len(height), -1):
            if height[jj] > max_right:
                max_right = height[jj]
            min_val = min(dp[jj], max_right)
            if min_val > height[jj]:
                summary = min_val - height[jj] + summary
        return summary


# 代码优化-使用双指针，时间一样48ms
class Solution:
    def trap(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        left_max = right_max = 0
        ans = 0

        while i < j:
            left_max = max(left_max, height[i])
            right_max = max(right_max, height[j])
            if left_max <= right_max:
                ans += (left_max - height[i])
                i += 1
            else:
                ans += (right_max - height[j])
                j -= 1
        return ans