# 解法1
class Solution:
    def getSum(self, a: int, b: int) -> int:
        return sum[a, b]

# 解法2-移位运算
class Solution:
    def getSum(self, a: int, b: int) -> int:
        carry = 0
        mask = 0xffffffff

        while b & mask != 0:
            carry = (a & b) << 1
            a = a ^ b
            b = carry

        return a & mask if b > mask else a
