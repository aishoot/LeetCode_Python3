"""
最大子串和
写得较好的博客：https://www.cnblogs.com/en-heng/p/3970231.html
"""


# 我的解法 - 动态规划 - 时间复杂度为O(n)，空间复杂度也为O(n)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
        return max(dp)


# 动态规划基础上的优化算法-Kadane算法 - 时间复杂度亦为O(n)，空间复杂度为O(1)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = -float("inf")
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            ans = max(ans, sum)
            if sum < 0:
                sum = 0
        return ans

# 优化2：
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        e = max_so_far = nums[0]
        for x in nums[1:]:
            e = max(x, e + x)
            max_so_far = max(max_so_far, e)
        return max_so_far


# 继续优化，优化3
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]
        return max(nums)

# 优化4
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] = max(nums[i], nums[i-1] + nums[i])
        return max(nums)
  

# 分治算法
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def divide_and_conquer(nums, i, j):
            if i == j - 1:
                return nums[i], nums[i], nums[i], nums[i]

            i_mid = i + (j - i) // 2
            a1, m1, b1, s1 = divide_and_conquer(nums, i, i_mid)
            a2, m2, b2, s2 = divide_and_conquer(nums, i_mid, j)

            a = max(a1, s1 + a2)
            b = max(b2, s2 + b1)
            m = max(m1, m2, b1 + a2)
            s = s1 + s2
            return a, m, b, s

        _, m, _, _ = divide_and_conquer(nums, 0, len(nums))
        return m
