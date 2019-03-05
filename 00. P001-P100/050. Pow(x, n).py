# 解法1 - 二分往下递归计算
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1 / self.myPow(x, -n)
        elif n == 0:
            return 1.0
        elif n % 2 == 0:
            return self.myPow(x * x, n / 2)
        else:
            return x * self.myPow(x, n - 1)

# 解法2-迭代版
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n
        pow = 1
        while n:
            # 判断奇偶的方法：奇数&1=1, 偶数&1=0
            if n & 1:  # 如果是奇数
                pow *= x
            x *= x
            n >>= 1
        return pow