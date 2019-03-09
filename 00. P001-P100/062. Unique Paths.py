# 解法1-我的代码-超时
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 0 or n == 0:
            return 0
        if (m == 1 and n == 2) or (m == 2 and n == 1):
            return 1
        if m == 1 and n == 1:
            return 1
        return self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)


# 优化版本-我的代码-使用动态规划
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1]*m for _ in range(n)]
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]


# 优化空间复杂度到O(N)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n
        for _ in range(m-1):
            for j in range(1, n):
                dp[j] += dp[j-1]
        return dp[-1]

# 一行代码解决问题
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return int(math.factorial(m-1+n-1) / (math.factorial(m-1) * math.factorial(n-1)))
