# 利用字符串作为中间处理
class Solution:
    def clumsy(self, N: int) -> int:
        a = list(map(str, range(N, 0, -1)))
        s = a[0]
        m = {0: '*', 1: '//', 2:'+', 3:'-'}
        for idx, ele in enumerate(a[1:]):
            s += m[idx%4] + ele
        return eval(s)

# 进一步简化代码
class Solution:
    def clumsy(self, N: int) -> int:
        op = itertools.cycle("*/+-")
        return eval("".join(str(x) + next(op) for x in range(N, 0, -1))[:-1])

# 解法2-将减法看作加法-递归调用
class Solution:
    def clumsy(self, N: int) -> int:
        def caltail(n):
            if n == 1: return -1
            if n == 2: return -2
            if n == 3: return -6
            if n == 4: return -5
            return caltail(n - 4) - n * (n - 1) // (n - 2) + (n - 3)

        if N == 1: return 1
        if N == 2: return 2
        if N == 3: return 6
        if N == 4: return 7
        return N * (N - 1) // (N - 2) + N - 3 + caltail(N - 4)
