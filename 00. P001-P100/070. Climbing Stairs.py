# 使用动态规划，时间和空间复杂度都是O(N)
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n
        dp = [1] * (n+1)
        for i in range(2, n+1):
            dp[i] = dp[i-2] + dp[i-1]
        return dp[-1]


# 优化空间复杂度到O(1)
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        first, second = 1, 2
        for i in range(3, n+1):
            third = first + second
            first = second
            second = third
        return second

# 利用斐波拉切数列的通向表达式时间复杂度可以是O(logN)，空间复杂度可以是O(1)
class Solution:
    def climbStairs(self, n: int) -> int:
        sqrt5 = math.sqrt(5)
        fibn = math.pow((1+sqrt5)/2, n+1) - math.pow((1-sqrt5)/2, n+1)
        return int(fibn/sqrt5)

# 计算pow时时间复杂度是O(logN)