# 最简单解法
class Solution:
    def mySqrt(self, x: int) -> int:
        return int(math.sqrt(x))
        # 或者return int(x**0.5)

# 解法2-二分法
class Solution:
    def mySqrt(self, x: int) -> int:
        low, hi = 0, x
        while low <= hi:
            mid = (low + hi) // 2
            if mid ** 2 <= x:
                low = mid + 1
            else:
                hi = mid - 1
        return int(low - 1)

# 牛顿法
"""
Newton's method:
g(x) = sqrt(x) = y, then
y^2 - x = 0 = f(y)
known x solve zero point for y
f'(y) = 2y
f(y) - f(y0) = f'(y0) * (y - y0)
if f(y1) = 0, then
y1 = y0-f(y0) / f'(y0)
then set y0 = y1, and iterate until abs(y1 - y0) < epsilon
"""
class Solution:
    def mySqrt(self, x: int) -> int:
        epsilon = 1E-6
        y0 = 1
        y1 = y0 - (y0**2 - x) / (2*y0)
        while abs(y1 - y0) > epsilon:
            y0 = y1
            y1 = y0 - (y0**2 - x) / (2*y0)
        return int(y1)

