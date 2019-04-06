# 暴力破解，代码超时
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                res = max(res, prices[j] - prices[i])
        return res

# 将时间复杂度优化到O(N),但时间还是很长
# 152 ms, faster than 5.59% of Python3
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        maxValue, temp = 0, [0]
        for i in range(len(prices)-2, -1, -1):
            maxValue = max(maxValue, prices[i+1])
            temp.insert(0, maxValue)
        for i in range(len(prices)-1):
            res = max(res, temp[i]-prices[i])
        return res

# 将insert换成效率更高的append，优化时间
# 52 ms, faster than 31.81% of Python3
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        maxValue, temp = 0, [0]
        for i in range(len(prices)-2, -1, -1):
            maxValue = max(maxValue, prices[i+1])
            temp.append(maxValue)
        for i in range(len(prices)-1):
            res = max(res, temp[len(prices)-i-1]-prices[i])
        return res

# 转换下思路，最优思路
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit, min_price = 0, float('inf')
        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(max_profit, profit)
        return max_profit