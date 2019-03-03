class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0

        while dividend >= divisor:
            temp, i = divisor, 1
            # 以下除数temp和商res指数级增长，肯定比每次都执行减操作快
            while dividend >= temp:
                dividend -= temp
                res += i
                i <<= 1
                temp <<= 1

        if not positive:
            res = -res

        return min(max(-2147483648, res), 2147483647)