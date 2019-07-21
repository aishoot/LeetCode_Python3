# 暴力但没法通过的解法
class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        res = 0
        for i in range(len(arr1)-1):
            for j in range(i+1, len(arr1)):
                value = abs(arr1[i] - arr1[j]) + abs(arr2[i] - arr2[j]) + abs(i - j)
                res = max(res, value)
        return res


# 其他解法1，276 ms, faster than 50.00% of Python3
class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        li = ((1, 1), (-1, 1), (1, -1), (-1, -1))
        minn = [1 << 31 for t in range(4)]
        sol = -1 << 31

        for i in range(len(arr1)):
            for t in range(4):
                val = li[t][0] * arr1[i] + li[t][1] * arr2[i] + i
                sol = max(sol, val - minn[t])
                minn[t] = min(minn[t], val)

        return sol

# 解法3
class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        res, n = 0, len(arr1)
        for p, q in [[1, 1], [1, -1], [-1, 1], [-1, -1]]:
            closest = p * arr1[0] + q * arr2[0] + 0
            for i in range(n):
                cur = p * arr1[i] + q * arr2[i] + i
                res = max(res, cur - closest)
                closest = min(closest, cur)
        return res


# 时间稍微短点
class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        n = len(arr1)
        rtn = 0
        for sign1 in [-1, 1]:
            for sign2 in [-1, 1]:
                b = []
                for i in range(n):
                    b.append(arr1[i] * sign1 + arr2[i] * sign2 + i)
                rtn = max(rtn, max(b) - min(b))
        return rtn

