# 我的代码，非常暴力，不推荐
class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        if K % 2 == 0 or K % 5 == 0:
            return -1
        r = 0
        for N in range(1, K + 1):
            r = (r * 10 + 1) % K
            if not r:
                return N

# 优化代码
class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        if K % 2 ==0 or K % 5==0:
            return -1
        module = 1
        for Ndigits in range(1, K+1):
            if module % K == 0:
                return Ndigits
            module = (module * 10 + 1) % K
        return 1234567890   # This line never executes