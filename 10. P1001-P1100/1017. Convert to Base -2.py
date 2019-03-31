# 做法类似于正数求余得到二进制的做法
class Solution:
    def baseNeg2(self, N: int) -> str:
        if N in [0, 1]:
            return str(N)
        if N % 2 == 0:
            return self.baseNeg2(N // -2) + '0'
        else:
            return self.baseNeg2((N - 1) // -2) + '1'

# 优化代码
class Solution:
    def baseNeg2(self, N: int) -> str:
        if N == 0 or N == 1:
            return str(N)
        return self.baseNeg2(-(N >> 1)) + str(N & 1)

