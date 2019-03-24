# 动态规划，递推公式不太容易想出来
class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        dp = [0] * len(A)
        dp[0] = A[0]
        for i in range(1, len(dp)):
            dp[i] = max(A[i] + A[i - 1] - 1, dp[i - 1] - A[i - 1] + A[i] - 1)
        return max(dp)

# 进一步优化，不需要 O(n) space
class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        cur, ans = A[0], A[0]
        for i in range(1, len(A)):
            cur = max(A[i] + A[i-1]-1, cur-A[i-1]+A[i]-1)
            ans = max(ans, cur)
        return ans

# 进一步简化为
class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        cur = res = 0
        for a in A:
            res = max(res, cur + a)
            cur = max(cur, a) - 1
        return res