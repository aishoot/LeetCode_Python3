# 最开始解法-暴力解法，超时
class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        res = []
        for ii in range(1, len(A)+1):
            bin_str = A[:ii]
            num_str = ''.join([str(i) for i in bin_str])
            shi = int(num_str, 2)
            if shi % 5 == 0:
                res.append(True)
            else:
                res.append(False)
        return res

# 上面的计算没有有效利用前一次的计算结果
# 优化后的解法
class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        res, num = [], 0
        for ii in range(len(A)):
            num = (num << 1) + A[ii]
            res.append(True) if num % 5 == 0 else res.append(False)
        return res


# 空间复杂度优化到O(1)
class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        num = 0
        for i in range(len(A)):
            num = (num << 1) + A[i]
            A[i] = (num % 5 == 0)
        return A

# 时间更省
class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        for i in range(1, len(A)):
            A[i] += A[i - 1] * 2 % 5  # 可以不用考虑A[i]，反正要么1/0
        return [a % 5 == 0 for a in A]